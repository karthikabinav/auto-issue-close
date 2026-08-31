"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    return any(label in TARGET_LABELS for label in labels)

def close_issues_example():
    # Example logic: fetch open issues, if label in TARGET_LABELS then close
    # Uses GitHub API: PATCH /repos/{owner}/{repo}/issues/{number} with state=closed
    print("Checking issues for labels:", TARGET_LABELS)

if __name__ == "__main__":
    close_issues_example()
