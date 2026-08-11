#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'.
"""
import os
import sys
TARGET_LABELS = {"completed", "wontfix"}
def should_close(labels):
    return bool(set(labels) & TARGET_LABELS)
# See full implementation in repo history
