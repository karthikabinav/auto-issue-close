"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER")
REPO = os.getenv("GITHUB_REPO")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def close_issues():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    close_issues()
