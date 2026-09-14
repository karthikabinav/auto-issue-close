#!/usr/bin/env python3
"""Automation script to automatically close issues labeled as completed or wontfix."""
import os
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

if __name__ == "__main__":
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
