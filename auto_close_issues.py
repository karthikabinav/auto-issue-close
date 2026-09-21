#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, requests
OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}
def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    for issue in requests.get(url, headers=headers).json():
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"{url}/{issue[number]}", headers=headers, json={"state": "closed"})
if __name__ == "__main__":
    main()
