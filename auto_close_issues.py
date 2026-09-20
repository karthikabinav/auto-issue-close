"""Automatically close issues labeled completed or wontfix."""
import os
from github import Github

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
