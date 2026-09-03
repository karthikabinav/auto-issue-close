"""
Automated Issue Closing Script
Closes GitHub issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    return any(label in AUTO_CLOSE_LABELS for label in labels)

def close_issues_example():
    """
    Example logic for GitHub automation.
    In production, this would use GitHub API to list and close issues:
    - List open issues in karthikabinav/auto-issue-close
    - If labels contain completed or wontfix, close the issue
    """
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)

if __name__ == "__main__":
    close_issues_example()
