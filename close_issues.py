#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import sys

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

if __name__ == "__main__":
    # Example usage with the GitHub API (token in GITHUB_TOKEN):
    # List open issues, close those with CLOSE_LABELS.
    # This script is paired with .github/workflows/auto-close-issues.yml,
    # which closes issues on the labeled/opened event.
    print("Close issues labeled: completed or wontfix")
    print(f"Labels that trigger closing: {sorted(CLOSE_LABELS)}")
