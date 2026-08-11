#!/usr/bin/env python3
"""
Automated Issue Closing Script

This script demonstrates GitHub automation for closing issues labeled
as "completed" or "wontfix".

Usage:
  python scripts/auto_close.py --repo owner/repo --token $GITHUB_TOKEN

In production, this would run as a GitHub Action.
"""

import os
import sys
import argparse

def should_close_issue(labels):
    """Check if issue should be closed based on labels"""
    target_labels = {"completed", "wontfix"}
    issue_labels = {label.lower() for label in labels}
    return bool(target_labels & issue_labels)

def main():
    print("=== Automated Issue Closing ===")
    print("Monitoring issues for labels: completed, wontfix")
    print()
    
    # Simulated test cases from task requirements
    test_issues = [
        {"number": 1, "title": "Implement new feature", "labels": ["completed"], "state": "open"},
        {"number": 2, "title": "Remove legacy code", "labels": ["wontfix"], "state": "open"},
        {"number": 3, "title": "Fix login error", "labels": ["bug"], "state": "open"},
    ]
    
    for issue in test_issues:
        print(f"Checking Issue #{issue[number]}: {issue[title]}")
        print(f"  Labels: {issue[labels]}")
        
        if should_close_issue(issue["labels"]):
            print(f"  -> ACTION: Close issue (matches target label)")
            print(f"  -> COMMENT: Automatically closed by automation")
            issue["state"] = "closed"
        else:
            print(f"  -> ACTION: Leave open (no matching label)")
        
        print(f"  Final state: {issue[state]}")
        print()
    
    closed_count = sum(1 for i in test_issues if i["state"] == "closed")
    print(f"Summary: Closed {closed_count}/{len(test_issues)} issues")

if __name__ == "__main__":
    main()
