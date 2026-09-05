"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    return any(lbl in TARGET_LABELS for lbl in labels)

# Example usage in automation:
# For each open issue, if should_close(issue_labels): close the issue.
# See .github/workflows/auto-close.yml for GitHub Actions automation.

if __name__ == "__main__":
    print("Automation script for closing labeled issues.")
    print(f"Target labels: {TARGET_LABELS}")
    sample_issues = [
        {"title": "Implement new feature", "labels": ["completed"]},
        {"title": "Remove legacy code", "labels": ["wontfix"]},
        {"title": "Fix login error", "labels": ["bug"]},
    ]
    for issue in sample_issues:
        action = "CLOSE" if should_close(issue["labels"]) else "KEEP OPEN"
        print(f"{action}: {issue["title"]} labels={issue["labels"]}")
