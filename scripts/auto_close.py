# Auto-close script for GitHub issues labeled as completed or wontfix
# This script demonstrates automation logic for closing labeled issues

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue should be auto-closed based on labels."""
    return any(label.lower() in TARGET_LABELS for label in labels)

def close_issues_example():
    """Example logic - in GitHub Actions this would call GitHub API to close issues."""
    # Example usage:
    # For each open issue, if should_close_issue(issue_labels): close issue
    print("Checking issues for labels:", TARGET_LABELS)
    print("Issues with completed/wontfix will be closed automatically via workflow .github/workflows/auto-close.yml")

if __name__ == "__main__":
    close_issues_example()
