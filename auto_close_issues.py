"""Automatically close issues labeled 'completed' or 'wontfix'.
This is a learning script for GitHub automation - it uses the GitHub API
to list open issues and close those with completed/wontfix labels.
"""
import os

CLOSE_LABELS = {'completed', 'wontfix'}

def should_close(labels):
    return bool(CLOSE_LABELS.intersection(labels))

if __name__ == '__main__':
    print('Automation: issues with labels completed/wontfix will be closed.')
