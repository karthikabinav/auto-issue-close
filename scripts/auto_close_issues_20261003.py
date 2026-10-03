"""Automatically close issues labeled completed or wontfix."""
import os

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(labels))

# In GitHub Actions this logic is implemented in
# .github/workflows/auto-close-labeled-issues-20261003-0148.yml
# which closes an issue when it is opened or labeled with
# completed or wontfix. Issues with other labels such as bug remain open.
