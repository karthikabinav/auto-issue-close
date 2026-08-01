#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix".
"""
import os
from github import Github  # PyGithub

REPO = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    if not TOKEN:
        print("GITHUB_TOKEN not set, skipping.")
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    for issue in repo.get_issues(state="open"):
        label_names = {label.name for label in issue.labels}
        if label_names & LABELS_TO_CLOSE:
            matched = label_names & LABELS_TO_CLOSE
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {matched})")
            issue.create_comment(f"Automatically closing issue labeled as {"".join(matched)}.")
            issue.edit(state="closed")
        else:
            print(f"Skipping issue #{issue.number}: {issue.title} (labels: {label_names})")

if __name__ == "__main__":
    main()
