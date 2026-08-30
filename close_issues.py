"""
Automated Issue Closing script
Closes issues labeled as completed or wontfix.
"""
import os
# This script is intended to run via GitHub Actions.
# Logic: list open issues, if label is completed or wontfix, close it.
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in AUTO_CLOSE_LABELS for l in labels)

if __name__ == "__main__":
    print("Automation script: closes issues labeled as completed or wontfix")
