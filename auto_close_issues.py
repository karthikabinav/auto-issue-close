"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_example():
    """
    Example logic using GitHub API (pseudo-code):
    - List open issues
    - If label in AUTO_CLOSE_LABELS, close issue via PATCH /repos/{owner}/{repo}/issues/{number} with state=closed
    """
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)

if __name__ == "__main__":
    close_issues_example()
