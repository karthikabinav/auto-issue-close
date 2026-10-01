"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
import os
from github import Github

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    g = Github(token) if token else Github()
    repo = g.get_repo(repo_name)
    target_labels = {"completed", "wontfix"}
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & target_labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
