#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix"
"""

import os
import requests

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_OWNER = "karthikabinav"
REPO_NAME = "auto-issue-close"

CLOSE_LABELS = ["completed", "wontfix"]

def get_open_issues():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open&per_page=100"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def close_issue(issue_number, label):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"state": "closed"}
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()
    
    comment_url = f"{url}/comments"
    comment_data = {"body": f"This issue was automatically closed because it was labeled as **{label}**."}
    requests.post(comment_url, headers=headers, json=comment_data)
    print(f"Closed issue #{issue_number} labeled as {label}")

def main():
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable not set")
        return
    
    issues = get_open_issues()
    closed_count = 0
    
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = [label["name"] for label in issue.get("labels", [])]
        for close_label in CLOSE_LABELS:
            if close_label in labels:
                close_issue(issue["number"], close_label)
                closed_count += 1
                break
    
    print(f"\nAutomation complete! Closed {closed_count} issues.")

if __name__ == "__main__":
    main()
