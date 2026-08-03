"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

REPO_NAME = "karthikabinav/auto-issue-close"
LABELS_TO_CLOSE = {"completed", "wontfix"}

def close_labeled_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        raise ValueError("GITHUB_TOKEN environment variable not set")
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.create_comment(f"Automatically closing this issue because it was labeled as **{list(labels & LABELS_TO_CLOSE)[0]}**.")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: {issue.title} (labels: {labels})")

if __name__ == "__main__":
    close_labeled_issues()
