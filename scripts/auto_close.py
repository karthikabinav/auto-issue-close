#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Configuration
REPO_NAME = "karthikabinav/auto-issue-close"
TARGET_LABELS = {"completed", "wontfix"}

def close_labeled_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            # Safety: only close if matching labels, do not close bug or other labels
            issue.edit(state="closed")
            issue.create_comment(f"Automatically closed as labeled with {labels & TARGET_LABELS}")

if __name__ == "__main__":
    close_labeled_issues()
