# Auto-close issues labeled completed or wontfix
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return any(label in LABELS_TO_CLOSE for label in labels)
