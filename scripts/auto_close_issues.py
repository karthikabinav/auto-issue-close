#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'.
Intended to be run via GitHub Actions on issues events (opened/labeled),
or on a schedule / manually for testing.
"""
import os
import sys
import requests

API_URL = "https://api.github.com"
TARGET_LABELS = {"completed", "wontfix"}

def get_headers():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set, exiting.")
        sys.exit(1)
    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def list_open_issues(owner, repo, headers):
    issues = []
    page = 1
    while True:
        resp = requests.get(f"{API_URL}/repos/{owner}/{repo}/issues", headers=headers, params={"state": "open", "per_page": 100, "page": page})
        resp.raise_for_status()
        data = resp.json()
        if not data:
            break
        # Filter out pull requests
        issues.extend([i for i in data if "pull_request" not in i])
        page += 1
    return issues

def close_issue(owner, repo, number, headers):
    # Add comment
    requests.post(f"{API_URL}/repos/{owner}/{repo}/issues/{number}/comments", headers=headers, json={"body": "Automatically closed because this issue is labeled as completed or wontfix."})
    # Close
    resp = requests.patch(f"{API_URL}/repos/{owner}/{repo}/issues/{number}", headers=headers, json={"state": "closed", "state_reason": "completed"})
    resp.raise_for_status()
    print(f"Closed issue #{number}")

def main():
    repo_full = os.environ.get("GITHUB_REPOSITORY")
    if repo_full and "/" in repo_full:
        owner, repo = repo_full.split("/", 1)
    else:
        owner = os.environ.get("REPO_OWNER", "karthikabinav")
        repo = os.environ.get("REPO_NAME", "auto-issue-close")
    headers = get_headers()
    for issue in list_open_issues(owner, repo, headers):
        labels = {l["name"].lower() for l in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            close_issue(owner, repo, issue["number"], headers)

if __name__ == "__main__":
    main()
