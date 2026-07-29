import os
from github import Github

# Script to automatically close issues labeled as "completed" or "wontfix"
# Usage: Set GITHUB_TOKEN env var and run python close_issues.py

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    if not TOKEN:
        print("GITHUB_TOKEN not set, dry-run mode: listing logic only")
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment(f"Automatically closing this issue as it is labeled {labels & LABELS_TO_CLOSE}.")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
