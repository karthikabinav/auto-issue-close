# Automation script to automatically close issues labeled as completed or wontfix

import os

# Labels that trigger automatic closing
CLOSE_LABELS = ["completed", "wontfix"]

def should_close(issue_labels):
    return any(label in CLOSE_LABELS for label in issue_labels)

def close_issues(issues):
    for issue in issues:
        labels = [label.get("name") if isinstance(label, dict) else label for label in issue.get("labels", [])]
        if should_close(labels):
            print(f"Closing issue #{issue[number]}: {issue[title]} (labels: {labels})")
            # In a real GitHub workflow, this would call update_issue with state=closed
            # e.g. update_issue(owner, repo, issue[number], state=closed)
        else:
            print(f"Keeping open issue #{issue[number]}: {issue[title]} (labels: {labels})")

if __name__ == "__main__":
    print("Automation: closing issues labeled completed or wontfix")
