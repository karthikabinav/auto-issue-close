"""
Automated Issue Closing Script

This script automatically closes GitHub issues labeled as 'completed' or 'wontfix'.
Designed for the auto-issue-close repository.
"""
import os
from github import Github

# Configuration
TARGET_LABELS = {"completed", "wontfix"}
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")

def close_labeled_issues():
    if not TOKEN:
        print("GITHUB_TOKEN not set - running in dry-run mode, listing logic only")
        print(f"Would close issues with labels: {TARGET_LABELS}")
        return

    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    open_issues = repo.get_issues(state="open")

    for issue in open_issues:
        labels = {label.name for label in issue.labels}
        matching = labels.intersection(TARGET_LABELS)
        if matching:
            label = matching.pop()
            print(f"Closing issue #{issue.number}: {issue.title} (label: {label})")
            issue.create_comment(
                f"Automatically closing this issue because it was labeled as \"{label}\"."
            )
            issue.edit(state="closed", state_reason="completed")

if __name__ == "__main__":
    close_labeled_issues()
