#!/usr/bin/env python3
"""Close issues labeled completed or wontfix via GitHub API."""
import os
import requests

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO = "auto-issue-close"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
TARGET_LABELS = {"completed", "wontfix"}
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}

def main():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open&per_page=100"
    issues = requests.get(url, headers=HEADERS, timeout=30).json()
    for issue in issues:
        labels = {label.get("name", "") for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            number = issue["number"]
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{number}", headers=HEADERS, json={"state": "closed"}, timeout=30)
            print(f"Closed #{number}: {issue.get(chr(39)+chr(39), chr(39))}")

if __name__ == "__main__":
    main()
