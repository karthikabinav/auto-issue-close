#!/usr/bin/env python3
"""
Automated Issue Closing Script

This script demonstrates GitHub automation logic to close issues
labeled as "completed" or "wontfix".

It can be used with GitHub Actions or PyGithub library.
"""

import os

def should_close_issue(labels):
    """Check if issue should be closed based on labels"""
    close_labels = {"completed", "wontfix"}
    issue_labels = set(labels)
    return bool(close_labels & issue_labels)

def main():
    # Example logic for GitHub Actions using github-script
    print("GitHub Automation for Closing Labeled Issues")
    print("Labels that trigger auto-close: completed, wontfix")
    
    test_cases = [
        (["completed"], True),
        (["wontfix"], True),
        (["bug"], False),
        (["completed", "enhancement"], True),
        ([], False)
    ]
    
    for labels, expected in test_cases:
        result = should_close_issue(labels)
        status = "✓ PASS" if result == expected else "✗ FAIL"
        print(f"{status}: labels={labels} -> close={result} (expected {expected})")

if __name__ == "__main__":
    main()
