"""Script to automatically close issues labeled completed or wontfix."""
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

if __name__ == "__main__":
    print("Close issues with labels: completed or wontfix")
