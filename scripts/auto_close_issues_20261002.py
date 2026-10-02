"""Automatically close issues labeled completed or wontfix.

Intended to be run by GitHub Actions on issue labeled/opened events.
The .github/workflows/auto-close-labeled-issues-20261002-2130.yml
workflow implements the same logic with actions/github-script.
"""
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return any(label in LABELS_TO_CLOSE for label in labels)
