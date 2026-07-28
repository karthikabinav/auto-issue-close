"""
Automated Issue Closing Script
Closes issues labeled completed or wontfix
"""
import os
import sys
import requests

TARGET_LABELS = {"completed", "wontfix"}

def get_issues(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    params = {"state": "open", "per_page": 100}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def close_issue(owner, repo, issue_number, token, label):
    base = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    comment_url = base + "/comments"
    body = f"Auto closing issue labeled {label}"
    requests.post(comment_url, headers=headers, json={"body": body})
    resp = requests.patch(base, headers=headers, json={"state": "closed"})
    resp.raise_for_status()
    return resp.json()

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set", file=sys.stderr)
        sys.exit(1)
    issues = get_issues(args.owner, args.repo, token)
    closed = 0
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {lab["name"] for lab in issue.get("labels", [])}
        inter = TARGET_LABELS.intersection(labels)
        if inter:
            lab = list(inter)[0]
            print(f"Closing {issue[number]} {issue[title]} label {lab}")
            close_issue(args.owner, args.repo, issue["number"], token, lab)
            closed += 1
        else:
            print(f"Skip {issue[number]} {issue[title]}")
    print(f"Closed {closed}")

if __name__ == "__main__":
    main()
