# Automated Issue Closing Script
# Closes issues labeled as "completed" or "wontfix"

"""
This script demonstrates GitHub automation for closing labeled issues.
It can be used as a reference for learning GitHub automation workflows.

Usage:
    python auto_close_issues.py

Logic:
    - List open issues in the repository
    - If issue has label "completed" or "wontfix", close it
    - Otherwise, leave it open
"""

TARGET_LABELS = {"completed", "wontfix"}

# Example pseudo-code using GitHub API (via MCP tools):
# 1. list_issues(owner, repo, state="open")
# 2. for issue in issues:
#        labels = {label["name"] for label in issue["labels"]}
#        if labels & TARGET_LABELS:
#            update_issue(owner, repo, issue["number"], state="closed")
#            print(f"Closed issue #{issue[number]}: {issue[title]}")

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    return bool(set(labels) & TARGET_LABELS)

if __name__ == "__main__":
    # Example test cases
    test_issues = [
        {"title": "Implement new feature", "labels": ["completed"]},
        {"title": "Remove legacy code", "labels": ["wontfix"]},
        {"title": "Fix login error", "labels": ["bug"]},
    ]
    for issue in test_issues:
        action = "CLOSE" if should_close(issue["labels"]) else "KEEP OPEN"
        print(f"{action}: {issue[title]} {issue[labels]}")
