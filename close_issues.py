"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Configuration
REPO_NAME = "karthikabinav/auto-issue-close"
LABELS_TO_CLOSE = ["completed", "wontfix"]

def close_labeled_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set, using unauthenticated mode (read-only demo)")
        return

    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")

    for issue in issues:
        label_names = [label.name for label in issue.labels]
        if any(label in LABELS_TO_CLOSE for label in label_names):
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {label_names})")
            issue.create_comment(f"Automatically closing issue as it was labeled `{[l for l in label_names if l in LABELS_TO_CLOSE][0]}`.")
            issue.edit(state="closed")

if __name__ == "__main__":
    close_labeled_issues()
