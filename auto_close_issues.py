#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os
import sys
import requests

CLOSE_LABELS = {"completed", "wontfix"}

def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return 1
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    issues_url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    resp = requests.get(issues_url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            number = issue["number"]
            print(f"Closing issue #{number}: {issue[title]} labels={labels}")
            r = requests.patch(f"https://api.github.com/repos/{repo}/issues/{number}", headers=headers, json={"state": "closed"})
            r.raise_for_status()
    return 0

if __name__ == "__main__":
    sys.exit(main())
