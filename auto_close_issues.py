"""Automatically close issues labeled completed or wontfix."""
import os
import requests

OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO = "auto-issue-close"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
CLOSE_LABELS = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {"Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    for issue in requests.get(url, headers=headers, timeout=30).json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            requests.patch(f"{url.split(chr(63))[0]}/{issue[chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)]}", headers=headers, json={"state": "closed"}, timeout=30)

if __name__ == "__main__":
    main()
