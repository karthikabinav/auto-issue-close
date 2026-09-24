"""Script to automatically close issues labeled as completed or wontfix."""
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in TARGET_LABELS for label in labels)

if __name__ == "__main__":
    examples = [("Implement new feature", ["completed"]), ("Remove legacy code", ["wontfix"]), ("Fix login error", ["bug"])]
    for title, labels in examples:
        print(title, "close" if should_close(labels) else "keep open")
