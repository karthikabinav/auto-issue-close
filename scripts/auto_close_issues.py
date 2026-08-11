#!/usr/bin/env python3
"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix"
"""

import os
import sys
from github import Github

# Configuration
g = Github(os.environ.get("GITHUB_TOKEN"))
repo_name = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")

LABELS_TO_CLOSE = ["completed", "wontfix"]

def close_labeled_issues():
    """Close issues with matching labels"""
    repo = g.get_repo(repo_name)
    open_issues = repo.get_issues(state="open")
    
    closed_count = 0
    kept_open_count = 0
    
    print(f"Scanning repository: {repo_name}")
    print(f"Labels that trigger auto-close: {LABELS_TO_CLOSE}")
    print("-" * 60)
    
    for issue in open_issues:
        issue_labels = [label.name.lower() for label in issue.labels]
        matching_labels = [label for label in issue_labels if label in LABELS_TO_CLOSE]
        
        print(f"\nIssue #{issue.number}: \"{issue.title}\"")
        print(f"  Labels: {issue_labels if issue_labels else "none"}")
        
        if matching_labels:
            print(f"  Action: CLOSING (matched labels: {matching_labels})")
            issue.edit(state="closed", state_reason="completed")
            closed_count += 1
        else:
            print(f"  Action: Keeping OPEN")
            kept_open_count += 1
    
    print("\n" + "=" * 60)
    print(f"SUMMARY: Closed {closed_count} issues, kept {kept_open_count} open")
    return closed_count

if __name__ == "__main__":
    try:
        closed = close_labeled_issues()
        sys.exit(0 if closed >= 0 else 1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
