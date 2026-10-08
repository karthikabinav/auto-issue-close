"""Script to automatically close issues labeled as completed or wontfix."""
import os

CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    label_names = {label["name"] if isinstance(label, dict) else str(label) for label in labels}
    return bool(label_names & CLOSE_LABELS)

def main():
    print("Automation script to close issues labeled completed or wontfix")

if __name__ == "__main__":
    main()
