"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix"
"""
import os
from github import Github

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def main():
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set, running in dry-run mode")
        print(f"Would close issues in {REPO_NAME} with labels: {TARGET_LABELS}")
        return

    g = Github(GITHUB_TOKEN)
    repo = g.get_repo(REPO_NAME)
    
    open_issues = repo.get_issues(state="open")
    closed_count = 0
    
    for issue in open_issues:
        labels = {label.name for label in issue.labels}
        matching = labels.intersection(TARGET_LABELS)
        if matching:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {matching})")
            issue.create_comment(f"Automatically closing this issue because it was labeled as \"{list(matching)[0]}\".")
            issue.edit(state="closed")
            closed_count += 1
        else:
            print(f"Skipping issue #{issue.number}: {issue.title} (labels: {labels})")
    
    print(f"Done. Closed {closed_count} issues.")

if __name__ == "__main__":
    main()
