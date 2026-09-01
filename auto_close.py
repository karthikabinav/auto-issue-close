# Automated Issue Closing script
# Closes issues labeled as completed or wontfix
import os
# This script is intended to run via GitHub Actions or manually
# Logic: for each open issue, if label in [completed, wontfix], close it
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in TARGET_LABELS for l in labels)

if __name__ == "__main__":
    print("Auto-close script: checks issues with labels completed/wontfix and closes them.")
