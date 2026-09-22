#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
from github import Github

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
