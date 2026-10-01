# Automatically close issues labeled completed or wontfix
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return any(label in LABELS_TO_CLOSE for label in labels)

def close_issue_if_needed(issue):
    labels = [label.get("name") if isinstance(label, dict) else label for label in issue.get("labels", [])]
    return should_close(labels)
