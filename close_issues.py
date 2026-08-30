"""
Automation script to close issues labeled as completed or wontfix.

This script demonstrates GitHub automation for learning purposes.
It lists open issues and closes those with labels "completed" or "wontfix".

Usage: Configure with a GitHub token with repo scope.
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a target label."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & TARGET_LABELS)

def main():
    # Example logic - in real workflow, use PyGithub or GitHub API
    # from github import Github
    # g = Github(os.environ["GITHUB_TOKEN"])
    # repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    # for issue in repo.get_issues(state="open"):
    #     labels = [l.name for l in issue.get_labels()]
    #     if should_close_issue(labels):
    #         issue.create_comment(f"Closing as labeled with {[l for l in labels if l.lower() in TARGET_LABELS]}.")
    #         issue.edit(state="closed")
    #         print(f"Closed #{issue.number}: {issue.title}")
    print("Automation script loaded. Target labels:", TARGET_LABELS)

if __name__ == "__main__":
    main()
