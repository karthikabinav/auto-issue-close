import os
from github import Github

# Script to automatically close issues labeled as 'completed' or 'wontfix'
# Usage: Set GITHUB_TOKEN env var and run

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set, running in dry-run mode")
        return
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.create_comment(f"Auto-closing issue with labels: {', '.join(labels & TARGET_LABELS)}")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
