"""Automatically close issues labeled as completed or wontfix.

Usage:
  GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python auto_close_issues.py

This script lists open issues and closes any that have the labels
completed or wontfix. Issues with other labels (e.g. bug) are left open.
It mirrors the GitHub Actions workflow in
.github/workflows/auto-close-issues.yml.
"""
import json
import os
import urllib.request

CLOSE_LABELS = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        raise SystemExit("Set GITHUB_TOKEN and GITHUB_REPOSITORY")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        issues = json.load(resp)
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            print(f"Closing #{issue[number]}: {issue[title]} labels={labels}")
            data = json.dumps({"state": "closed"}).encode()
            req2 = urllib.request.Request(
                f"https://api.github.com/repos/{repo}/issues/{issue[number]}",
                data=data, headers={**headers, "Content-Type": "application/json"}, method="PATCH"
            )
            with urllib.request.urlopen(req2) as resp2:
                print(resp2.status)
        else:
            print(f"Leaving open #{issue[number]}: {issue[title]} labels={labels}")

if __name__ == "__main__":
    main()
