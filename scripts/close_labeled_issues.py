"""
Automation script to close issues labeled as 'completed' or 'wontfix'.

This script can be run manually or via GitHub Actions.
It lists open issues and closes those with target labels.
"""
import os

# Labels that trigger auto-close
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if any label matches TARGET_LABELS."""
    return any(label.lower() in TARGET_LABELS for label in labels)

def main():
    """
    Example logic using GitHub API (requires PyGithub or gh CLI).
    For GitHub Actions, the workflow .github/workflows/auto-close.yml handles this natively.
    """
    print(f"Checking for issues with labels: {TARGET_LABELS}")
    # In Actions, use:
    # gh issue list --label "completed" --state open --json number --jq '.[].number' | xargs -I {} gh issue close {}
    # gh issue list --label "wontfix" --state open --json number --jq '.[].number' | xargs -I {} gh issue close {}
    print("Use the accompanying GitHub Workflow to auto-close on label event.")

if __name__ == "__main__":
    main()
