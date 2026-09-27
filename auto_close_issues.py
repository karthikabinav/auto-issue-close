"""Automatically close issues labeled as completed or wontfix.

This script is provided for learning GitHub automation. The GitHub
Actions workflow in .github/workflows/auto-close-issues.yml performs
the same check automatically when an issue is opened or labeled.
"""

CLOSE_LABELS = {"completed", "wontfix"}


def should_close(labels):
    """Return True if any label means the issue should be closed."""
    return any(label in CLOSE_LABELS for label in labels)


# Example logic (used by the workflow via the GitHub API):
# if should_close([label.name for label in issue.labels]):
#     issue.edit(state="closed")
