# Automation script to close issues labeled completed or wontfix
import os

# This script is intended to be used with GitHub Actions or PyGithub
# TARGET_LABELS = {"completed", "wontfix"}
# For each open issue, if any label is in TARGET_LABELS, close the issue

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return any(label in TARGET_LABELS for label in issue_labels)

def close_labeled_issues(repo):
    for issue in repo.get_issues(state="open"):
        labels = [label.name for label in issue.labels]
        if should_close(labels):
            issue.edit(state="closed")

if __name__ == "__main__":
    print(should_close(["completed"]))  # True
    print(should_close(["wontfix"]))  # True
    print(should_close(["bug"]))  # False
    print("Automation logic ready. Integrate with GitHub API to list and close issues.")
