"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

REPO_NAME = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")

def main():
    if not TOKEN:
        print("GITHUB_TOKEN not set, running in dry-run mode - listing logic only")
    g = Github(TOKEN) if TOKEN else None
    repo = g.get_repo(REPO_NAME) if g else None

    target_labels = {"completed", "wontfix"}

    if repo:
        issues = repo.get_issues(state="open")
        for issue in issues:
            labels = {label.name for label in issue.labels}
            if labels & target_labels:
                matched = labels & target_labels
                print(f"Closing issue #{issue.number}: {issue.title} (labels: {matched})")
                issue.create_comment(f"Automatically closing this issue because it was labeled as **{next(iter(matched))}**.")
                issue.edit(state="closed", state_reason="completed" if "completed" in matched else "not_planned")
    else:
        print("Dry-run: Would close issues with labels:", target_labels)
        print("Example logic:")
        print("  for issue in repo.get_issues(state='open'):")
        print("      if any(label.name in ['completed', 'wontfix'] for label in issue.labels):")
        print("          issue.edit(state='closed')")

if __name__ == "__main__":
    main()
