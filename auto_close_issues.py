#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os
import requests

REPO = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
CLOSE_LABELS = {"completed", "wontfix"}

def main():
    resp = requests.get(f"https://api.github.com/repos/{REPO}/issues?state=open&per_page=100", headers=HEADERS, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            number = issue["number"]
            requests.patch(f"https://api.github.com/repos/{REPO}/issues/{number}", headers=HEADERS, json={"state": "closed"}, timeout=30).raise_for_status()
            print(f"Closed issue #{number}")

if __name__ == "__main__":
    main()
