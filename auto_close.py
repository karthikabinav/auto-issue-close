"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def close_labeled_issues():
    if not TOKEN:
        print("GITHUB_TOKEN not set, skipping")
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {l.name for l in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state="closed")
            issue.create_comment(f"Automatically closed because label is in {TARGET_LABELS}")

if __name__ == "__main__":
    close_labeled_issues()
