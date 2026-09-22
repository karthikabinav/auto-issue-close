"""Automatically close issues labeled completed or wontfix."""
import os
import requests

REPO_FULL = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
CLOSE_LABELS = {"completed", "wontfix"}

def main():
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    base = f"https://api.github.com/repos/{REPO_FULL}/issues"
    issues = requests.get(base, headers=headers, params={"state": "open"}, timeout=30).json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            requests.patch(f"{base}/{issue["number"]}", headers=headers, json={"state": "closed"}, timeout=30)

if __name__ == "__main__":
    main()
