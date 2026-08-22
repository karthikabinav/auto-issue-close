"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""
import os

# Example logic for automation - to be used in workflow or manually
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in TARGET_LABELS for label in labels)

if __name__ == "__main__":
    print("Auto-close script ready. Target labels:", TARGET_LABELS)
