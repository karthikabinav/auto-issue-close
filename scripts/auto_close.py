#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'.
"""
import os
from github import Github

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def close_labeled_issues():
    """
    Automatically close issues with labels 'completed' or 'wontfix'
    """
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set - running in dry-run mode")
        # Dry-run logic for local testing
        target_labels = {'completed', 'wontfix'}
        print(f"Would close issues with labels: {target_labels}")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    target_labels = {'completed', 'wontfix'}
    
    for issue in repo.get_issues(state='open'):
        labels = {label.name for label in issue.labels}
        if labels & target_labels:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.create_comment(
                f"Automatically closing this issue as it was labeled as '{', '.join(labels & target_labels)}'."
            )
            issue.edit(state='closed')

if __name__ == "__main__":
    close_labeled_issues()
