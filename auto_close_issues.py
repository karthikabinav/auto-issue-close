#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os
import requests

REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    if not REPO or not TOKEN:
        raise SystemExit("GITHUB_REPOSITORY and GITHUB_TOKEN are required")
    owner, repo = REPO.split("/", 1)
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    issues = requests.get(f"https://api.github.com/repos/{owner}/{repo}/issues?state=open", headers=headers, timeout=30).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue[chr(39)+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"}, timeout=30)
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
