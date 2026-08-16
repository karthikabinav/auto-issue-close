#!/usr/bin/env python3
"""
Automated Issue Closing Script
Automatically closes GitHub issues labeled as "completed" or "wontfix".
"""
import os
from github import Github

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
        labels = {label.name.lower() for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment("🤖 This issue was automatically closed because it has the `completed` or `wontfix` label.")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: labels {labels}")

if __name__ == "__main__":
    close_labeled_issues()
