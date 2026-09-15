# Automated Issue Closing
# Closes issues labeled as completed or wontfix

CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    return any(label.lower() in CLOSE_LABELS for label in labels)

# Example usage with GitHub API:
# - List open issues in the repository
# - For each issue, if should_close_issue(issue_labels): close the issue
# This script is intended as a learning example for GitHub automation.

if __name__ == "__main__":
    print("Check open issues and close those labeled completed or wontfix")
