# Automation script to close issues labeled as completed or wontfix
# This script is for educational purposes - review before running
# It lists open issues and closes those with target labels

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return bool(set(issue_labels) & TARGET_LABELS)

# Example usage with GitHub API:
# 1. List open issues in karthikabinav/auto-issue-close
# 2. For each issue, if labels intersect TARGET_LABELS, close it with a comment
# 3. Leave other labels (e.g., bug) open for manual triage

print("Script ready: closes issues labeled completed or wontfix")
