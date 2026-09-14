#!/usr/bin/env python3
"""
Automated Issue Closing script
Closes issues labeled as 'completed' or 'wontfix'.
"""
import os
import requests

REPO = os.getenv("GITHUB_REPOSITORY")  # format: owner/repo
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def list_open_issues(owner, repo):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def close_issue(owner, repo, issue_number):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {TOKEN}"} if TOKEN else {}
    data = {"state": "closed"}
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()

def main():
    if not REPO:
        print("GITHUB_REPOSITORY not set")
        return
    owner, repo = REPO.split("/")
    issues = list_open_issues(owner, repo)
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            print(f"Closing issue #{issue[number]} with labels {labels}")
            close_issue(owner, repo, issue["number"])

if __name__ == "__main__":
    main()
