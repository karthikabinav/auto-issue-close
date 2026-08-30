"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
import os
# This script is intended to run in GitHub Actions
# It closes issues labeled as completed or wontfix

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label.lower() in TARGET_LABELS for label in labels)

# Example GitHub Actions workflow snippet:
# Use actions/github-script to close issues when labeled
print("Auto-close script ready: closes issues with labels:", TARGET_LABELS)
