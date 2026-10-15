#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
from github import Github

CLOSE_LABELS = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_name:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY must be set")
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & CLOSE_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
            issue.edit(state="closed")
        else:
            print(f"Keeping open issue #{issue.number}: {issue.title} labels={labels}")

if __name__ == "__main__":
    main()
