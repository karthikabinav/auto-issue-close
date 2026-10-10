#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TARGET_LABELS = {"completed", "wontfix"}
BASE = f"https://api.github.com/repos/{REPO}"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}

def should_close_issue(labels):
    label_names = {label["name"] if isinstance(label, dict) else str(label) for label in labels}
    return bool(label_names & TARGET_LABELS)

def close_labeled_issues():
    resp = requests.get(f"{BASE}/issues?state=open&per_page=100", headers=HEADERS)
    resp.raise_for_status()
    for issue in resp.json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            number = issue["number"]
            r = requests.patch(f"{BASE}/issues/{number}", headers=HEADERS, json={"state": "closed"})
            print(f"Closed issue {number} status {r.status_code}")

if __name__ == "__main__":
    close_labeled_issues()
