import os
from github import Github

# This script automatically closes issues labeled as 'completed' or 'wontfix'
# Requires GITHUB_TOKEN environment variable

def auto_close_issues(repo_name):
    g = Github(os.getenv("GITHUB_TOKEN"))
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state="closed")
            issue.create_comment("Automatically closed as labeled as completed/wontfix")

if __name__ == "__main__":
    repo = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    auto_close_issues(repo)
