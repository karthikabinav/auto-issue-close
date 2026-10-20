"""Automatically close issues labeled as completed or wontfix."""
import os

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

if __name__ == "__main__":
    # Example usage with GitHub API via gh CLI / PyGithub would go here.
    # This script defines the logic: close issues whose labels include completed or wontfix.
    print("Close issues labeled as completed or wontfix")
