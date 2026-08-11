import os
from github import Github

"""
Automation script to automatically close issues labeled as completed or wontfix
"""

def auto_close_issues(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment("Automatically closed because it was labeled as completed or wontfix.")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: {issue.title} - no auto-close label")

if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if not token:
        print("GITHUB_TOKEN not set")
    else:
        auto_close_issues(repo_name, token)
