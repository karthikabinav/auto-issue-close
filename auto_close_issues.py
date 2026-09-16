"""Automatically close issues labeled completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = "auto-issue-close"
LABELS_TO_CLOSE = {"completed", "wontfix"}
TOKEN = os.getenv("GITHUB_TOKEN")

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
    resp = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open", headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue["number"]}", headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    main()
