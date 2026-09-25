"""Automatically close issues labeled completed or wontfix."""
import os
import requests
REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{REPO}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            number = issue["number"]
            patch_url = f"https://api.github.com/repos/{REPO}/issues/{number}"
            requests.patch(patch_url, headers=headers, json={"state": "closed"})
            print("Closed issue", number)

if __name__ == "__main__":
    main()
