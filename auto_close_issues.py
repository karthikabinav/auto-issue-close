"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Accept": "application/vnd.github+json"}
    if TOKEN:
        headers["Authorization"] = "token " + TOKEN
    url = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels.intersection(LABELS_TO_CLOSE):
            issue_url = "https://api.github.com/repos/" + OWNER + "/" + REPO + "/issues/" + str(issue.get("number"))
            requests.patch(issue_url, headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    main()
