"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
import sys
try:
    from github import Github
except ImportError:
    Github = None

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue has target label to auto-close."""
    label_names = {label.name.lower() if hasattr(label, "name") else str(label).lower() for label in labels}
    return bool(label_names & TARGET_LABELS)

def close_issues():
    if not TOKEN or Github is None:
        print("GITHUB_TOKEN not set or PyGithub not installed - dry run mode")
        print(f"Would close issues with labels: {TARGET_LABELS}")
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        if should_close_issue(issue.labels):
            print(f"Closing issue #{issue.number}: {issue.title} with labels {[l.name for l in issue.labels]}")
            issue.create_comment(f"Automatically closing this issue because it was labeled as `{[l.name for l in issue.labels if l.name.lower() in TARGET_LABELS][0]}`.")
            issue.edit(state="closed", state_reason="completed")

if __name__ == "__main__":
    close_issues()
