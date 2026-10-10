#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import sys
try:
    from github import Github
except ImportError:
    Github = None
CLOSE_LABELS = {"completed", "wontfix"}
def should_close(issue):
    labels = {label.name.lower() for label in issue.get_labels()}
    return bool(labels & CLOSE_LABELS)
def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_name:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
        sys.exit(1)
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        if should_close(issue):
            print(f"Closing issue #{issue.number}: {issue.title}")
            issue.edit(state="closed")
            issue.create_comment("Automatically closed because it is labeled as completed or wontfix.")
    print("Done.")
if __name__ == "__main__":
    main()
