#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os

LABELS_TO_CLOSE = {"completed", "wontfix"}
OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")

def should_close(labels):
    return bool(set(labels) & LABELS_TO_CLOSE)

# GitHub Actions workflow .github/workflows/auto-close.yml implements this logic:
# on issues labeled/opened, if label is completed or wontfix, close via github.rest.issues.update(state=closed)

if __name__ == "__main__":
    print(f"Monitoring {OWNER}/{REPO} for labels: {LABELS_TO_CLOSE}")
