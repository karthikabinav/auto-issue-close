# Automation script to close issues labeled as completed or wontfix
# This script is for educational purposes - review issues before closing
# Usage: Run manually after reviewing open issues

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    return any(label in TARGET_LABELS for label in labels)

# Example logic:
# 1. List open issues via GitHub API
# 2. For each issue, check labels
# 3. If label in TARGET_LABELS, close with comment explaining reason
# 4. Otherwise, leave open (e.g., bug reports need triage)

print("Script ready. Review issues manually before auto-closing.")
