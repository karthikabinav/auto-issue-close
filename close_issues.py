"""Script to automatically close issues labeled 'completed' or 'wontfix'."""
import os
import requests

LABELS_TO_CLOSE = {"completed", "wontfix"}

def close_issues(owner, repo, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels.intersection(LABELS_TO_CLOSE):
            requests.patch(issue["url"], json={"state": "closed"}, headers=headers)
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    owner = os.getenv("GITHUB_REPOSITORY_OWNER")
    repo = os.getenv("GITHUB_REPOSITORY", "/").split("/")[-1]
    token = os.getenv("GITHUB_TOKEN")
    if owner and repo and token:
        close_issues(owner, repo, token)
