#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, requests
REPO = os.getenv("GITHUB_REPOSITORY")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS = {"completed", "wontfix"}
def close_issues():
    headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
    issues = requests.get(f"https://api.github.com/repos/{REPO}/issues", headers=headers, params={"state": "open"}).json()
    for issue in issues:
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS:
            requests.patch(f"https://api.github.com/repos/{REPO}/issues/{issue['number']}" , headers=headers, json={"state": "closed"})
if __name__ == "__main__":
    close_issues()
