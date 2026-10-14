"""Automatically close issues labeled completed or wontfix."""
import os

# Labels that should trigger auto-closing
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

if __name__ == "__main__":
    print("Auto-close script: closes issues labeled completed or wontfix")
