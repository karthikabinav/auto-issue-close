"""
Automation script to close issues labeled as completed or wontfix.
"""
# This script demonstrates automation logic for closing labeled issues.
# In production, it would use the GitHub API to list and close issues.

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue should be auto-closed based on labels."""
    return any(label.lower() in TARGET_LABELS for label in labels)

def get_issues_to_close(issues):
    """Filter issues that should be closed."""
    return [issue for issue in issues if should_close_issue(issue.get("labels", []))]

if __name__ == "__main__":
    # Example usage - in real automation this would call GitHub API
    sample_issues = [
        {"title": "Implement new feature", "labels": ["completed"]},
        {"title": "Remove legacy code", "labels": ["wontfix"]},
        {"title": "Fix login error", "labels": ["bug"]},
    ]
    to_close = get_issues_to_close(sample_issues)
    for issue in to_close:
        print(f"Closing issue: {issue["title"]} with labels {issue["labels"]}")
