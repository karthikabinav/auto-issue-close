"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
    issues = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open", headers=headers).json()
    for issue in issues:
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)]}", headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    main()
