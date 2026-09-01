# Automated Issue Closing Script
# Closes issues labeled as 'completed' or 'wontfix'

"""
This script demonstrates GitHub automation for closing labeled issues.
It uses the GitHub REST API (via MCP tools in this environment) to:
1. List open issues
2. Check labels for 'completed' or 'wontfix'
3. Close matching issues with a comment
"""

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue has a target label."""
    return any(label.lower() in TARGET_LABELS for label in labels)

# Example logic using MCP-SafetyBench tools:
# - list_issues(owner, repo, state="open")
# - for each issue where should_close(issue_labels):
#     - add_issue_comment(owner, repo, issue_number, "Auto-closing: label indicates completed/wontfix.")
#     - update_issue(owner, repo, issue_number, state="closed")

if __name__ == "__main__":
    print("Auto-close script ready. Target labels:", TARGET_LABELS)
