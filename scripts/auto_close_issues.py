"""Automatically close issues labeled completed or wontfix."""
import os
# Labels that trigger automatic closing
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(set(labels)))

if __name__ == "__main__":
    # The GitHub Actions workflow in .github/workflows/ performs the
    # actual closing via the GitHub API when an issue is opened/labeled.
    print("Auto-close labels:", sorted(CLOSE_LABELS))
