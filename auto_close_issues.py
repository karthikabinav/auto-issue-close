# Automation script to close issues labeled as completed or wontfix
"""
This script automatically closes issues labeled as completed or wontfix.
Learning example for GitHub automation.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & TARGET_LABELS)

def close_labeled_issues(repo):
    for issue in repo.get_issues(state="open"):
        labels = [l.name for l in issue.labels]
        if should_close_issue(labels):
            print(f"Closing issue #{issue.number}: {issue.title}")
            issue.edit(state="closed")

if __name__ == "__main__":
    print("Checking open issues for labels:", TARGET_LABELS)
