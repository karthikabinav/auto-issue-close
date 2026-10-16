"""Automatically close issues labeled as completed or wontfix.

This script uses the GitHub REST API to list open issues in this
repository and close any issue that has the label completed or
wontfix. Issues with other labels, such as bug, are left open.

Usage:
    GITHUB_TOKEN=... GITHUB_REPOSITORY=owner/repo python close_issues.py
"""
import os
import sys
import urllib.request
import json

TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Set GITHUB_TOKEN and GITHUB_REPOSITORY environment variables")
        sys.exit(1)
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json", "User-Agent": "auto-issue-close"}
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        issues = json.load(resp)
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            print(f"Closing #{issue[number]}: {issue[title]} labels={sorted(labels)}")
            close_url = f"https://api.github.com/repos/{repo}/issues/{issue[number]}"
            data = json.dumps({"state": "closed"}).encode()
            close_req = urllib.request.Request(close_url, data=data, headers=headers, method="PATCH")
            with urllib.request.urlopen(close_req) as close_resp:
                close_resp.read()
        else:
            print(f"Leaving open #{issue[number]}: {issue[title]} labels={sorted(labels)}")

if __name__ == "__main__":
    main()
