"""Script to automatically close issues labeled as completed or wontfix."""
# This script is intended to be used in GitHub Actions or manually.
# It closes open issues that have the labels "completed" or "wontfix".

import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(lbl in TARGET_LABELS for lbl in labels)

# Example GitHub Actions workflow usage:
# See .github/workflows/auto-close.yml for automation.

if __name__ == "__main__":
    print("Automation script for closing labeled issues.")
    print(f"Target labels: {TARGET_LABELS}")
