#!/usr/bin/env python3
"""Automatically closes issues labeled as completed or wontfix."""
import os
import requests

REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    if not REPO or not TOKEN:
        raise SystemExit("GITHUB_REPOSITORY and GITHUB_TOKEN must be set")
    owner, repo = REPO.split("/")
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        label_names = [label["name"] for label in issue.get("labels", [])]
        if any(name in LABELS_TO_CLOSE for name in label_names):
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue["number"]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
