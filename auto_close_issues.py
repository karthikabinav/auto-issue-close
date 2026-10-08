# Automatically close issues labeled completed or wontfix.
import os
from github import Github

LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & LABELS_TO_CLOSE)

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_name:
        print("GITHUB_TOKEN and GITHUB_REPOSITORY must be set")
        return
    repo = Github(token).get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if should_close(labels):
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
