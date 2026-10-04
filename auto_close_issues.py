# Automation script to close issues labeled as completed or wontfix
# For each open issue, if it has label completed or wontfix, close it.
# Labels to close: completed, wontfix
# Other labels (e.g. bug) remain open.

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(labels))

if __name__ == "__main__":
    print("Close issues with labels: completed, wontfix")
