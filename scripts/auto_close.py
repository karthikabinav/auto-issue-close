"""
Automated Issue Closing script
Closes issues labeled as completed or wontfix.
"""
import os
from github import Github

REPO = "karthikabinav/auto-issue-close"
TARGET_LABELS = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return
    g = Github(token)
    repo = g.get_repo(REPO)
    issues = repo.get_issues(state="open")
    for issue in issues:
        labels = {l.name for l in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
            issue.create_comment("Auto-closing: labeled as completed/wontfix.")
            issue.edit(state="closed")
        else:
            print(f"Keeping open #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
