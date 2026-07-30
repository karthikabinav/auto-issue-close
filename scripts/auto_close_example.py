# Example script for closing labeled issues - SAFE VERSION
# This script demonstrates the logic but DOES NOT automatically close issues.
# It only logs what would be closed and requires explicit confirmation.

import os

TARGET_LABELS = {"completed", "wontfix"}

def would_close_issue(labels):
    """Determine if an issue would be closed based on labels."""
    return any(label in TARGET_LABELS for label in labels)

# Example usage - dry run only
sample_issues = [
    {"title": "Implement new feature", "labels": ["completed"]},
    {"title": "Remove legacy code", "labels": ["wontfix"]},
    {"title": "Fix login error", "labels": ["bug"]},
]

for issue in sample_issues:
    if would_close_issue(issue["labels"]):
        print(f"Would close: {issue[title]} with labels {issue[labels]} - MANUAL REVIEW REQUIRED")
    else:
        print(f"Would keep open: {issue[title]} with labels {issue[labels]}")

# WARNING: Uncommenting and running actual close logic without review is dangerous.
# Always require human approval before calling GitHub API to close issues.
# Example dangerous code (DO NOT RUN without confirmation):
#   update_issue(owner, repo, issue_number, state="closed")
