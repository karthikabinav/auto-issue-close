#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, requests
REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{REPO}/issues?state=open"
    for issue in requests.get(url, headers=headers).json():
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"{url}/{issue[chr(39)+chr(39)] if False else issue['number']}", headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    main()
