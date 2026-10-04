# Automation script to close issues labeled as completed or wontfix
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(labels))

if __name__ == "__main__":
    print("Close issues with labels: completed, wontfix")
