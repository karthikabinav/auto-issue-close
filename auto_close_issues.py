# Automated Issue Closing
# Closes issues labeled as completed or wontfix

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(TARGET_LABELS.intersection(set(labels)))

def auto_close_issues(issues):
    closed = []
    for issue in issues:
        labels = [label["name"] if isinstance(label, dict) else label for label in issue.get("labels", [])]
        if should_close(labels):
            # In production this would call the GitHub API to close the issue
            # e.g. update_issue(state="closed")
            closed.append(issue["number"])
    return closed

if __name__ == "__main__":
    print("Script to automatically close issues labeled completed or wontfix")
