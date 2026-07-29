"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def auto_close_issues():
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set. Running in dry-run mode - listing matching issues would be closed.")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)

    print(f"Checking open issues in {REPO_NAME} for labels: {TARGET_LABELS}")
    open_issues = repo.get_issues(state="open")
    closed_count = 0

    for issue in open_issues:
        labels = {label.name for label in issue.labels}
        matching = labels.intersection(TARGET_LABELS)
        if matching:
            label_name = matching.pop()
            print(f"Closing issue #{issue.number}: '{issue.title}' (label: {label_name})")
            issue.create_comment(f"Automatically closing this issue because it was labeled as `{label_name}`.")
            issue.edit(state="closed", state_reason="completed")
            closed_count += 1

    print(f"Done. Closed {closed_count} issue(s).")

if __name__ == "__main__":
    auto_close_issues()
