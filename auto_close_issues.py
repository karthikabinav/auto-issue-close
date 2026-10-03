# Script to automatically close issues labeled as completed or wontfix
# Labels to auto-close
CLOSE_LABELS = ["completed", "wontfix"]

def should_close(issue_labels):
    return any(label in CLOSE_LABELS for label in issue_labels)

# Example usage with GitHub MCP tools:
# 1. List open issues in the repository
# 2. For each issue, check its labels
# 3. If it has "completed" or "wontfix", update its state to "closed"
# Issues labeled "bug" (or other labels) remain open.
