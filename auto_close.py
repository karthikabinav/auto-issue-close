"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github  # Requires PyGithub

# Configuration
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def main():
    if not TOKEN:
        print("GITHUB_TOKEN not set - running in dry-run mode")
        print(f"Would close issues in {REPO_NAME} with labels: {TARGET_LABELS}")
        return

    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    issues = repo.get_issues(state="open")
    
    for issue in issues:
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            matched = labels & TARGET_LABELS
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {matched})")
            issue.create_comment(f"✅ Automatically closed because label is: **{matched.pop()}**.")
            issue.edit(state="closed", state_reason="completed")

if __name__ == "__main__":
    main()
