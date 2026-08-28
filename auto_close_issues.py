# Automation script to close issues labeled as completed or wontfix
"""
This script automatically closes issues labeled as completed or wontfix.
Learning example for GitHub automation.
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & TARGET_LABELS)

def close_issues_example():
    """
    Example logic using GitHub API (pseudo-code):
    - list open issues
    - for each issue, if label in TARGET_LABELS, update state to closed
    """
    print("Checking open issues for labels:", TARGET_LABELS)
    # Example with PyGithub:
    # from github import Github
    # g = Github(os.getenv("GITHUB_TOKEN"))
    # repo = g.get_repo("karthikabinav/auto-issue-close")
    # for issue in repo.get_issues(state="open"):
    #     labels = [l.name for l in issue.labels]
    #     if should_close_issue(labels):
    #         print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
    #         issue.edit(state="closed", state_reason="completed")
    pass

if __name__ == "__main__":
    close_issues_example()
