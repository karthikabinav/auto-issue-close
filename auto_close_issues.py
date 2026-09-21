#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    base = f"https://api.github.com/repos/{OWNER}/{REPO}/issues"
    resp = requests.get(base, headers=headers, params={"state": "open"}, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            patch = requests.patch(f"{base}/{issue[chr(39)+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"}, timeout=30)
            patch.raise_for_status()
            print(f"Closed #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
