"""Automation script that closes GitHub issues labeled as completed or wontfix.

This script lists open issues in the repository and closes any issue
that has a label matching CLOSE_LABELS.
"""

import argparse
import sys
import urllib.request
import json

# Labels that trigger automatic issue closing
CLOSE_LABELS = {"completed", "wontfix"}

API_ROOT = "https://api.github.com"


def list_open_issues(owner, repo, token):
    url = f"{API_ROOT}/repos/{owner}/{repo}/issues?state=open&per_page=100"
    request = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    })
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read())


def close_issue(owner, repo, issue_number, token):
    url = f"{API_ROOT}/repos/{owner}/{repo}/issues/{issue_number}"
    data = json.dumps({"state": "closed"}).encode()
    request = urllib.request.Request(url, data=data, method="PATCH", headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(request):
        pass


def main():
    parser = argparse.ArgumentParser(description="Auto-close issues labeled completed or wontfix.")
    parser.add_argument("owner", help="Repository owner")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("token", help="GitHub personal access token")
    args = parser.parse_args()

    issues = list_open_issues(args.owner, args.repo, args.token)
    closed = 0
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            close_issue(args.owner, args.repo, issue["number"], args.token)
            print(f"Closed issue #{issue[number]}: {issue[title]}")
            closed += 1
        else:
            print(f"Skipped issue #{issue[number]}: {issue[title]}")
    print(f"Done. {closed} issue(s) closed.")


if __name__ == "__main__":
    sys.exit(main())
