#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix. Intended for use via GitHub Actions with GITHUB_TOKEN."""
import os
CLOSE_LABELS = {"completed", "wontfix"}
# Workflow .github/workflows/auto-close.yml implements the closing logic using actions/github-script.
print(CLOSE_LABELS)
