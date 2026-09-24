"""
Automation script to close GitHub issues labeled as completed or wontfix.
Usage: python auto_close_issues.py --owner OWNER --repo REPO --token TOKEN
"""
import argparse
import urllib.request
import urllib.error
import json

TARGET_LABELS = {"completed", "wontfix"}
API_BASE = "https://api.github.com"

def api_request(url, token, method="GET", data=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "auto-issue-close-script"
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return json.loads(resp.read().decode())

def list_open_issues(owner, repo, token):
    url = f"{API_BASE}/repos/{owner}/{repo}/issues?state=open&per_page=100"
    issues = api_request(url, token)
    # filter out pull requests
    return [i for i in issues if "pull_request" not in i]

def close_issue(owner, repo, token, issue_number, matched_label):
    url = f"{API_BASE}/repos/{owner}/{repo}/issues/{issue_number}"
    api_request(url, token, method="PATCH", data={"state": "closed", "state_reason": "completed"})
    comment_url = f"{API_BASE}/repos/{owner}/{repo}/issues/{issue_number}/comments"
    api_request(comment_url, token, method="POST", data={"body": f"Automatically closed because it was labeled as `{matched_label}`."})
    print(f"Closed #{issue_number} (label: {matched_label})")

def main():
    parser = argparse.ArgumentParser(description="Auto-close labeled issues")
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--token", required=True)
    args = parser.parse_args()
    issues = list_open_issues(args.owner, args.repo, args.token)
    for issue in issues:
        labels = [l["name"] if isinstance(l, dict) else l for l in issue.get("labels", [])]
        matched = TARGET_LABELS.intersection(labels)
        if matched:
            label = matched.pop()
            close_issue(args.owner, args.repo, args.token, issue["number"], label)
        else:
            print(f"Skipping #{issue["number"]}: labels={labels}")

if __name__ == "__main__":
    main()
