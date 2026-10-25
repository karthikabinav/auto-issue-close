# Script to automatically close issues labeled completed or wontfix
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

def close_labeled_issues(issues, update_issue):
    closed = []
    for issue in issues:
        labels = [label["name"] if isinstance(label, dict) else label for label in issue.get("labels", [])]
        if issue.get("state") == "open" and should_close(labels):
            update_issue(issue["number"], state="closed")
            closed.append(issue["number"])
    return closed
