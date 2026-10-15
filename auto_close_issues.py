#!/usr/bin/env python3
"""Close GitHub issues labeled completed or wontfix.

Automation script: iterates open issues and closes those
labeled completed or wontfix. Issues with other labels
(e.g. bug) are left open.
"""
import os

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

if __name__ == "__main__":
    print("Automation script: closes issues with labels:", sorted(CLOSE_LABELS))
