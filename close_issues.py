#!/usr/bin/env python3
"""
Automation script to close issues labeled as completed or wontfix.
"""
import os
from github import Github

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & TARGET_LABELS)

def main():
    token = os.environ.get("GITHUB_TOKEN")
    g = Github(token) if token else Github()
    repo = g.get_repo(os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close"))
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state="closed")
    print("Done.")

if __name__ == "__main__":
    main()
