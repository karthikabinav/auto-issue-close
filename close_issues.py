# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix
import os

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

if __name__ == "__main__":
    print("Script to automatically close issues labeled as completed or wontfix")
    print(f"Target labels: {CLOSE_LABELS}")
