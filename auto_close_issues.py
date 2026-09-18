"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.environ.get("GITHUB_OWNER", "karthikabinav")
REPO = os.environ.get("GITHUB_REPO", "auto-issue-close")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"} if TOKEN else {}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)numberchr(39)] if False else issue["number"]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
