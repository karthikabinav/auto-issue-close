"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}

def should_close(labels):
    return bool(set(labels) & LABELS_TO_CLOSE)

def main():
    issues = requests.get(f"https://api.github.com/repos/{REPO}/issues?state=open", headers=headers).json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if should_close(labels):
            requests.patch(f"https://api.github.com/repos/{REPO}/issues/{issue["number"]}", headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    main()
