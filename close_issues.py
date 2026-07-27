"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Configuration
REPO_NAME = "karthikabinav/auto-issue-close"
TARGET_LABELS = {"completed", "wontfix"}
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def close_labeled_issues():
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set, running in dry-run mode")
        return
    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            matched = labels & TARGET_LABELS
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {matched})")
            issue.create_comment(f"Automatically closing this issue because it was labeled as **{matched.pop()}**.")
            issue.edit(state="closed", state_reason="completed")

if __name__ == "__main__":
    close_labeled_issues()
