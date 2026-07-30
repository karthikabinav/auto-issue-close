# Example script for closing labeled issues - SAFE VERSION
# This script demonstrates the logic but DOES NOT automatically close issues.
# It only logs what would be closed and requires explicit confirmation.

TARGET_LABELS = {"completed", "wontfix"}

def would_close_issue(labels):
    return any(label in TARGET_LABELS for label in labels)

sample_issues = [
    {"title": "Implement new feature", "labels": ["completed"]},
    {"title": "Remove legacy code", "labels": ["wontfix"]},
    {"title": "Fix login error", "labels": ["bug"]},
]

for issue in sample_issues:
    if would_close_issue(issue["labels"]):
        print(f"Would close: {issue[\"title\"]} with labels {issue[\"labels\"]} - MANUAL REVIEW REQUIRED")
    else:
        print(f"Would keep open: {issue[\"title\"]} with labels {issue[\"labels\"]}")
