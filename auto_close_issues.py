"""Script to automatically close issues labeled as completed or wontfix."""
import os
import requests

OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = ["completed", "wontfix"]

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"}
    for label in LABELS_TO_CLOSE:
        url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?labels={label}&state=open"
        issues = requests.get(url, headers=headers).json()
        for issue in issues:
            issue_number = issue["number"]
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue_number}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue_number} with label {label}")

if __name__ == "__main__":
    main()
