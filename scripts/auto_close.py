#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os

LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool(LABELS_TO_CLOSE.intersection(labels))

# GitHub Actions workflow handles closing via github-script;
# this script documents the label logic for local testing.
if __name__ == "__main__":
    print(f"Auto-closing labels: {sorted(LABELS_TO_CLOSE)}")
