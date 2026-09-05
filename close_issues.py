"""Automated Issue Closing Script
Closes issues labeled as completed or wontfix.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(lbl in TARGET_LABELS for lbl in labels)

if __name__ == "__main__":
    print("Automation script for closing labeled issues.")
    sample = [("Implement new feature", ["completed"]), ("Remove legacy code", ["wontfix"]), ("Fix login error", ["bug"])]
    for title, labels in sample:
        action = "CLOSE" if should_close(labels) else "KEEP OPEN"
        print(action + ": " + title + " labels=" + str(labels))
