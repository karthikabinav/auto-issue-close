"""Automatically close issues labeled completed or wontfix."""
import os
import requests

REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    issues = requests.get(f"https://api.github.com/repos/{REPO}/issues?state=open", headers=headers).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{REPO}/issues/{issue[chr(39) if False else 39 - 39 + 39] if False else issue["number"]}", headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
