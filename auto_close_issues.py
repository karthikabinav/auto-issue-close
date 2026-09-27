"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

CLOSING_LABELS = {"completed", "wontfix"}

def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    response = requests.get(f"https://api.github.com/repos/{repo}/issues", params={"state": "open"}, headers=headers, timeout=30)
    response.raise_for_status()
    for issue in response.json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSING_LABELS:
            close = requests.patch(f"https://api.github.com/repos/{repo}/issues/{issue[chr(35-13)+chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)] if False else issue["number"]}", json={"state": "closed"}, headers=headers, timeout=30)
            close.raise_for_status()
            print(f"Closed #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
