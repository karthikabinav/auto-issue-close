# Automation script to close issues labeled as completed or wontfix
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(set(labels)))

def close_issue_if_needed(issue):
    labels = [label["name"] if isinstance(label, dict) else label for label in issue.get("labels", [])]
    if should_close(labels):
        return "closed"
    return "open"

if __name__ == "__main__":
    print("Close issues with labels: completed, wontfix")
