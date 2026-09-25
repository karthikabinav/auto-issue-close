#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.environ.get("GITHUB_OWNER", "karthikabinav")
REPO = os.environ.get("GITHUB_REPO", "auto-issue-close")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    resp = requests.get(url, headers=headers, params={"state": "open", "per_page": 100})
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            r = requests.patch(f"{url}/{issue[chr(39)numberchr(39)]}" if False else f"{url}/{issue["number"]}", headers=headers, json={"state": "closed"})
            r.raise_for_status()
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
