import os
import requests

"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""

REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO_NAME = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

TARGET_LABELS = {"completed", "wontfix"}
API_BASE = "https://api.github.com"

def get_open_issues():
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}
    params = {"state": "open"}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def close_issue(issue_number):
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"} if GITHUB_TOKEN else {}
    data = {"state": "closed"}
    resp = requests.patch(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()

def main():
    issues = get_open_issues()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue[
umber\]} - {issue[	itle\]} with labels {labels}")
            if GITHUB_TOKEN:
                close_issue(issue[
umber\])
            else:
                print("DRY RUN: GITHUB_TOKEN not set, skipping actual close")
        else:
            print(f"Skipping issue #{issue[
umber\]} - {issue[	itle\]} with labels {labels}")

if __name__ == "__main__":
    main()
