import os
from github import Github

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            closing_labels = labels & LABELS_TO_CLOSE
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment(f"Automatically closing issue with labels: {closing_labels}")
            issue.edit(state="closed", state_reason="completed")
        else:
            print(f"Skipping issue #{issue.number}: {issue.title} - labels {labels} not in {LABELS_TO_CLOSE}")

if __name__ == "__main__":
    main()
