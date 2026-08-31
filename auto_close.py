"""
Automation script to close issues labeled as completed or wontfix.
Learning example for GitHub automation.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in TARGET_LABELS for l in labels)

def close_issues_example():
    # Example logic: fetch open issues, if label in TARGET_LABELS then close
    # Using GitHub API: PATCH /repos/{owner}/{repo}/issues/{number} with state=closed
    print("Checking issues for labels:", TARGET_LABELS)

if __name__ == "__main__":
    close_issues_example()
