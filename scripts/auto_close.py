# Automation script to close issues labeled as completed or wontfix
# This script is intended to be used in GitHub Actions workflow
# It checks issue labels and closes matching issues

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    return any(label in TARGET_LABELS for label in labels)

def close_issue(owner, repo, issue_number):
    """Placeholder for GitHub API call to close issue."""
    # In workflow, uses github.rest.issues.update with state closed
    print(f"Closing {owner}/{repo}#{issue_number}")

if __name__ == "__main__":
    # Example usage
    print("Auto-close script ready for labels: completed, wontfix")
