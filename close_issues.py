"""Script to automatically close issues labeled as completed or wontfix."""

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

def close_labeled_issues(issues, close_func):
    closed = []
    for issue in issues:
        labels = [label["name"] if isinstance(label, dict) else label for label in issue.get("labels", [])]
        if should_close(labels):
            close_func(issue["number"])
            closed.append(issue["number"])
    return closed

if __name__ == "__main__":
    print("This script closes open issues labeled completed or wontfix via the GitHub workflow / API.")
