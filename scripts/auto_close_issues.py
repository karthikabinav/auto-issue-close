"""
Automation script to close issues labeled as completed or wontfix.
"""
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    return bool(set(labels) & AUTO_CLOSE_LABELS)

# Example usage with GitHub API:
# For each open issue, if any label in AUTO_CLOSE_LABELS, close it via:
#   PATCH /repos/{owner}/{repo}/issues/{number} with state=closed
print("Automation script loaded: will close issues labeled as completed or wontfix")
