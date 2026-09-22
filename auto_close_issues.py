#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.environ.get("GITHUB_OWNER")
REPO = os.environ.get("GITHUB_REPO", "auto-issue-close")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open&per_page=100"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed #{issue[number]}")

if __name__ == "__main__":
    main()
