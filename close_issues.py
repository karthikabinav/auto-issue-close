# Automated Issue Closing Script
# Closes issues labeled as 'completed' or 'wontfix'

import os
import requests

LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(issue):
    labels = [label["name"] if isinstance(label, dict) else label for label in issue.get("labels", [])]
    return any(label in LABELS_TO_CLOSE for label in labels)

def close_labeled_issues(owner, repo, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for issue in response.json():
        if should_close(issue):
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue[number]}"
            requests.patch(close_url, json={"state": "closed"}, headers=headers)
            print(f"Closed issue #{issue[number]}: {issue[title]}")

if __name__ == "__main__":
    owner = os.getenv("GITHUB_OWNER", "karthikabinav")
    repo = os.getenv("GITHUB_REPO", "auto-issue-close")
    token = os.getenv("GITHUB_TOKEN", "")
    close_labeled_issues(owner, repo, token)
