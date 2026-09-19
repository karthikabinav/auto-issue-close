"""Automatically close issues labeled as completed or wontfix."""
import os
from github import Github

REPO = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def main():
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing #{issue.number} {issue.title} labels={labels}")
            issue.create_comment("Automatically closing this issue as completed/wontfix.")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
