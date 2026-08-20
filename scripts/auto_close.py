import os
import requests

"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix"
"""

REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO_NAME = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

LABELS_TO_CLOSE = {"completed", "wontfix"}
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

def get_open_issues():
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}
    resp = requests.get(API_URL, params={"state": "open", "per_page": 100}, headers=headers)
    resp.raise_for_status()
    return resp.json()

def close_issue(issue_number):
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}"
    data = {"state": "closed", "state_reason": "completed"}
    resp = requests.patch(url, json=data, headers=headers)
    resp.raise_for_status()
    # add comment
    comment_url = f"{url}/comments"
    requests.post(comment_url, json={"body": f"Automatically closing issue #{issue_number} with label completed/wontfix"}, headers=headers)
    print(f"Closed issue #{issue_number}")

def main():
    issues = get_open_issues()
    for issue in issues:
        labels = {label["name"].lower() for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            print(f"Closing issue #{issue[number]} titled {issue[title]} with labels {labels}")
            try:
                close_issue(issue["number"])
            except Exception as e:
                print(f"Failed to close {issue[number]}: {e}")
        else:
            print(f"Skipping issue #{issue[number]} - labels {labels} not in close set")

if __name__ == "__main__":
    main()
