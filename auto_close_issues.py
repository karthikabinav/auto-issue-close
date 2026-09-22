#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
LABELS_TO_CLOSE = {"completed", "wontfix"}
# GitHub Actions workflow (.github/workflows/auto-close-issues.yml) uses this logic:
# on issues labeled, if label is completed or wontfix, close the issue via GitHub API.
print(LABELS_TO_CLOSE)
