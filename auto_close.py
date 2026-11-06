"""
Automation script to close GitHub issues labeled as completed or wontfix.
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & TARGET_LABELS)

def main():
    # Example logic for GitHub automation
    # In real workflow, this would call GitHub API to list and close issues
    print("Checking issues with labels:", TARGET_LABELS)

if __name__ == "__main__":
    main()
