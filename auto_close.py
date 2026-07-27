"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# Alternatively using GitHub REST API via PyGithub or requests
# This script demonstrates logic for auto-closing issues

CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue should be closed based on labels."""
    label_names = {label.name if hasattr(label, 'name') else label for label in labels}
    return bool(label_names & CLOSE_LABELS)

def close_issues(repo_name, token=None):
    """Close open issues with specified labels."""
    token = token or os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set, running in dry-run mode")
        return
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        if should_close_issue(issue.labels):
            print(f"Closing issue #{issue.number}: {issue.title} - labels: {[l.name for l in issue.labels]}")
            issue.create_comment(f"Automatically closing this issue because it was labeled as **{,.join([l.name for l in issue.labels if l.name in CLOSE_LABELS])}**.")
            issue.edit(state="closed")
        else:
            print(f"Keeping open issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    # Example usage
    # close_issues("karthikabinav/auto-issue-close")
    print("Auto-close script loaded. Labels that trigger close:", CLOSE_LABELS)
    print("Use close_issues(repo_name) to execute.")
