#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os
import requests

REPO = os.getenv("GITHUB_REPOSITORY")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS = {"completed", "wontfix"}

def close_issues():
    headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
    response = requests.get(f"https://api.github.com/repos/{REPO}/issues", headers=headers, params={"state": "open"})
    issues = response.json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS:
            number = issue["number"]
            url = f"https://api.github.com/repos/{REPO}/issues/{number}"
            requests.patch(url, headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    close_issues()
