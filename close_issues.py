"""Script to automatically close issues labeled as completed or wontfix."""
from github import Github
import os

TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
