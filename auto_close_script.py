"""Automatically close issues labeled as completed or wontfix.

Used/documented alongside the GitHub Actions workflow in
.github/workflows/auto-close-issues-automation-2026-09.yml which
triggers on issue labeling and closes the issue when the label
is 'completed' or 'wontfix'.
"""
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool(LABELS_TO_CLOSE.intersection(labels))
