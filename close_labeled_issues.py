"""Automation script to close GitHub issues labeled as completed or wontfix.

Usage:
  python close_labeled_issues.py --owner OWNER --repo REPO --token GITHUB_TOKEN

This script lists open issues and closes those with labels completed or wontfix.
"""
import argparse
import json
import urllib.request

CLOSE_LABELS = {"completed", "wontfix"}

def github_api(method, url, token, data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
        body = json.dumps(data).encode()
    else:
        body = None
    with urllib.request.urlopen(req, body) as resp:
        return json.loads(resp.read().decode())

def should_close(labels):
    names = {l.get("name", "").lower() for l in labels}
    return bool(names & CLOSE_LABELS)

def main():
    parser = argparse.ArgumentParser(description="Close issues labeled completed or wontfix")
    parser.add_argument("--owner", required=True)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--token", required=True)
    args = parser.parse_args()
    base = f"https://api.github.com/repos/{args.owner}/{args.repo}"
    issues = github_api("GET", f"{base}/issues?state=open&per_page=100", args.token)
    for issue in issues:
        if "pull_request" in issue:
            continue
        if should_close(issue.get("labels", [])):
            num = issue["number"]
            title = issue["title"]
            print(f"Closing #{num}: {title}")
            url = f"{base}/issues/{num}"
            github_api("PATCH", url, args.token, {"state": "closed"})

if __name__ == "__main__":
    main()
