"""Close issues labeled completed or wontfix."""
import os
import sys

# This script is intended to be used with GitHub Actions / API.
# It checks issue labels and closes the issue if labeled completed or wontfix.
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & LABELS_TO_CLOSE)

if __name__ == "__main__":
    labels = sys.argv[1:] if len(sys.argv) > 1 else []
    print(f"Labels: {labels} -> close={should_close(labels)}")
