"""
Automation script to close GitHub issues labeled as completed or wontfix.

This script demonstrates logic for GitHub automation learning:
- List open issues
- Check labels
- Close issues with label completed or wontfix
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has target labels."""
    label_names = {label.lower() for label in labels}
    return bool(label_names & TARGET_LABELS)

def main():
    print("Checking open issues for labels:", TARGET_LABELS)
    # In real automation, use PyGithub or GitHub API:
    # from github import Github
    # g = Github(os.environ["GITHUB_TOKEN"])
    # repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    # for issue in repo.get_issues(state="open"):
    #     labels = [l.name for l in issue.labels]
    #     if should_close_issue(labels):
    #         print(f"Closing issue #{issue.number}: {issue.title}")
    #         issue.edit(state="closed")
    # For learning demo, just show logic:
    test_cases = [
        (["completed"], True),
        (["wontfix"], True),
        (["bug"], False),
    ]
    for labels, expected in test_cases:
        result = should_close_issue(labels)
        print(f"Labels {labels} -> close={result} (expected {expected})")

if __name__ == "__main__":
    main()
