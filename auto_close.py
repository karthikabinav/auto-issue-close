#!/usr/bin/env python3
"""
Automation script to automatically close issues labeled as 'completed' or 'wontfix'.

This script is intended as a learning example for GitHub automation.
It can be used in GitHub Actions or run manually with a GitHub token.
"""
import os

# Labels that should trigger auto-closing
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_example():
    """
    Example logic for GitHub Actions workflow:
    - Trigger on issues labeled event
    - If label is completed or wontfix, close the issue via API
    """
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
    # In a real workflow, you would:
    # 1. List open issues via GitHub API
    # 2. For each issue, call should_close_issue(issue_labels)
    # 3. If True, PATCH /repos/{owner}/{repo}/issues/{number} with state=closed
    # See .github/workflows/auto-close.yml for a complete Actions example.

if __name__ == "__main__":
    close_issues_example()
