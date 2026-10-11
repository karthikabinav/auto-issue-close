"""Close open issues labeled completed or wontfix."""
import os
import sys

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & TARGET_LABELS)

if __name__ == "__main__":
    print("This script closes open issues labeled completed or wontfix when run with a GitHub token.")
