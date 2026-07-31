import os
from github import Github

# Automation script to automatically close issues labeled as completed or wontfix
def close_labeled_issues(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment(f"Automatically closing issue labeled as {labels}")
            issue.edit(state="closed")
        else:
            print(f"Keeping open issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    repo = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    token = os.getenv("GITHUB_TOKEN")
    if token:
        close_labeled_issues(repo, token)
    else:
        print("GITHUB_TOKEN not set - script ready")
