# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix

"""
This script demonstrates GitHub automation for closing labeled issues.
Logic:
- List open issues
- If issue has label completed or wontfix, close it
"""

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    return any(label in TARGET_LABELS for label in labels)

if __name__ == "__main__":
    print("Checking open issues for labels:", TARGET_LABELS)
