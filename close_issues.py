import os
import requests

# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix

REPO = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")

labels_to_close = ["completed", "wontfix"]

owner, repo = REPO.split("/")
url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}

response = requests.get(url, headers=headers)
if response.status_code == 200:
    issues = response.json()
    for issue in issues:
        issue_labels = [l["name"] for l in issue.get("labels", [])]
        if any(label in issue_labels for label in labels_to_close):
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue[number]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue[number]}")
