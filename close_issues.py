"""Automatically close issues labeled as completed or wontfix."""
import os

# Labels that trigger automatic closing
CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if an issue has a completed or wontfix label."""
    label_names = {label["name"] if isinstance(label, dict) else str(label) for label in labels}
    return bool(label_names & CLOSE_LABELS)

def get_issues_to_close(issues):
    """Filter issues that should be closed based on their labels."""
    return [issue for issue in issues if should_close_issue(issue.get("labels", []))]

if __name__ == "__main__":
    print("Script to automatically close issues labeled completed or wontfix")
    print("Closing issues with labels:", CLOSE_LABELS)
