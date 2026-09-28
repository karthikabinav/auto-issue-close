"""Automatically close issues labeled completed or wontfix."""
import os

LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool({label.lower() for label in labels} & LABELS_TO_CLOSE)

# GitHub Actions workflow (.github/workflows/close-issues.yml) triggers this
# logic on issues:labeled events; the workflow equivalent is:
# if: github.event.label.name == 'completed' || github.event.label.name == 'wontfix'
# steps use actions/github-script to call issues.update(state='closed').

if __name__ == "__main__":
    print("Auto-close labels:", ", ".join(sorted(LABELS_TO_CLOSE)))
