"""Automatically close issues labeled as completed or wontfix."""
import os, sys
LABELS_TO_CLOSE = {"completed", "wontfix"}
# This script is used by the GitHub Actions workflow; it documents the automation logic.
print(LABELS_TO_CLOSE)
