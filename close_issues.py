"""
Automation script to automatically close issues labeled as completed or wontfix
"""
import os

# This script is intended to be used with GitHub API or GitHub Actions
# It closes issues labeled as completed or wontfix

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue should be closed based on labels"""
    label_names = {label if isinstance(label, str) else label.get("name", "") for label in labels}
    return bool(TARGET_LABELS.intersection(label_names))

def close_issues_demo():
    """Demo function showing logic"""
    print("Checking issues for labels: completed, wontfix")
    # In production, this would use GitHub API to list and close issues
    # Example: github.rest.issues.update(..., state="closed")
    pass

if __name__ == "__main__":
    close_issues_demo()
