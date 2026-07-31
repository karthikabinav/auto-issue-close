#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""
import os
import requests

def close_labeled_issues(owner, repo, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    issues = resp.json()
    for issue in issues:
        labels = [l["name"] for l in issue.get("labels", [])]
        if "completed" in labels or "wontfix" in labels:
            issue_number = issue["number"]
            print(f"Closing issue #{issue_number}: {issue['title']} (labels: {labels})")
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
            close_resp = requests.patch(close_url, headers=headers, json={"state": "closed"})
            if close_resp.status_code == 200:
                print(f"Successfully closed #{issue_number}")
                comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}/comments"
                requests.post(comment_url, headers=headers, json={"body": f"Automatically closed because label is `{'completed' if 'completed' in labels else 'wontfix'}`."})
            else:
                print(f"Failed to close #{issue_number}: {close_resp.text}")

if __name__ == "__main__":
    owner = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
    else:
        close_labeled_issues(owner, repo, token)
