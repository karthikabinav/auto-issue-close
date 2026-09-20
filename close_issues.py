"""Automatically close issues labeled as completed or wontfix."""
import os
from github import Github

TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            issue.create_comment("Automatically closing this issue as completed/wontfix.")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
