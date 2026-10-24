"""Script to automatically close issues labeled 'completed' or 'wontfix'."""

import os
import requests

OWNER = "karthikabinav"
REPO = "auto-issue-close"
CLOSE_LABELS = {"completed", "wontfix"}


def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"} if token else {}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for issue in response.json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            number = issue["number"]
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{number}"
            requests.patch(close_url, json={"state": "closed"}, headers=headers)
            print(f"Closed issue #{number}: {issue[title]}")


if __name__ == "__main__":
    main()
