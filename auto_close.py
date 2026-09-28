# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix

import os
from github import Github

# Configuration
REPO_NAME = "karthikabinav/auto-issue-close"
TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return
    g = Github(token)
    repo = g.get_repo(REPO_NAME)
    for issue in repo.get_issues(state="open"):
        labels = {l.name for l in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.edit(state="closed")
        else:
            print(f"Keeping open issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
