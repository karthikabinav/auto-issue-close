# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix

import os

AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue should be auto-closed based on labels."""
    label_names = {label.lower() if isinstance(label, str) else label.get("name", "").lower() for label in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_example():
    """Example logic for GitHub automation - used in workflow."""
    print("Checking issues for auto-close labels: completed, wontfix")
    # In GitHub Actions, this logic is implemented via .github/workflows/auto-close.yml
    # This script documents the intended behavior for learning purposes.
    pass

if __name__ == "__main__":
    close_issues_example()
