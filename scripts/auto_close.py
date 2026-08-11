#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'.
"""
import os
import sys

try:
    from github import Github
except ImportError:
    Github = None

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue):
    labels = {label.name.lower() for label in issue.labels}
    return bool(labels & TARGET_LABELS)

def close_labeled_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token or Github is None:
        print("GITHUB_TOKEN not set or PyGithub not installed - dry run mode")
        print(f"Would close issues in {REPO_NAME} labeled {TARGET_LABELS}")
        return
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        if should_close(issue):
            print(f"Closing issue #{issue.number}: {issue.title} labels={[l.name for l in issue.labels]}")
            issue.create_comment("Automatically closed because it was labeled as completed or wontfix.")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: labels={[l.name for l in issue.labels]}")

if __name__ == "__main__":
    close_labeled_issues()
