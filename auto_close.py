import os
from github import Github

# Script to automatically close issues labeled as completed or wontfix
# Usage: python auto_close.py

def auto_close_issues(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state='open')
    for issue in issues:
        labels = [label.name for label in issue.labels]
        if 'completed' in labels or 'wontfix' in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state='closed')
            issue.create_comment("Automatically closing this issue due to label: " + ", ".join(labels))

if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if token:
        auto_close_issues(repo_name, token)
    else:
        print("GITHUB_TOKEN not set. Set token to run automation.")
