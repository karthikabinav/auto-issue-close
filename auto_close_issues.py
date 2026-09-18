import os
from github import Github

# Automation script to close issues labeled as completed or wontfix
REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
TARGET_LABELS = {"completed", "wontfix"}

def main():
    if not TOKEN:
        print("GITHUB_TOKEN not set")
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment("Automatically closing this issue as it is labeled as completed or wontfix.")
            issue.edit(state="closed")
        else:
            print(f"Keeping open issue #{issue.number}: {issue.title} with labels {labels}")

if __name__ == "__main__":
    main()
