"""Automation script to close issues labeled completed or wontfix."""
import os
# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in AUTO_CLOSE_LABELS for l in labels)

def close_issues(owner, repo):
    # Placeholder for GitHub API logic:
    # list open issues, if label in AUTO_CLOSE_LABELS then close via PATCH /repos/{owner}/{repo}/issues/{number} state=closed
    print(f"Checking open issues in {owner}/{repo} for labels {AUTO_CLOSE_LABELS}")

if __name__ == "__main__":
    close_issues("karthikabinav", "auto-issue-close")
