"""Script to automatically close issues labeled as completed or wontfix."""
import os
from github import Github

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            issue.create_comment("Automatically closing this issue because it is labeled as completed or wontfix.")
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
