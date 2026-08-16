#!/usr/bin/env python3
"""
Automated Issue Closing script
Closes issues labeled as completed or wontfix
"""
import os
from github import Github

# This script can be used as a GitHub Action or standalone
# It automatically closes issues labeled as completed or wontfix

def auto_close_issues(owner, repo, token=None):
    g = Github(token) if token else Github()
    repository = g.get_repo(f"{owner}/{repo}")
    issues = repository.get_issues(state="open")
    for issue in issues:
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title} with labels {labels}")

if __name__ == "__main__":
    # Example usage
    # Set GITHUB_TOKEN env variable for authentication
    owner = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo_name = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
    token = os.getenv("GITHUB_TOKEN")
    auto_close_issues(owner, repo_name, token)
