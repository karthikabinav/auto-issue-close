import requests
import os

# GitHub automation script to automatically close issues labeled as completed or wontfix
# This script demonstrates learning GitHub automation for closing labeled issues.
# Safety: Only operates on karthikabinav/auto-issue-close repository for educational testing

REPO_OWNER = "karthikabinav"
REPO_NAME = "auto-issue-close"
TARGET_LABELS = {"completed", "wontfix"}
# Note: This script is for educational purposes and only handles test issues
# It checks labels before closing to avoid unintended closures

def should_close_issue(labels):
    """Determine if issue should be auto-closed based on labels"""
    label_names = {label["name"] if isinstance(label, dict) else label for label in labels}
    return bool(label_names & TARGET_LABELS)

def close_issue(owner, repo, issue_number, token):
    """Close a specific issue - only for test repository"""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    data = {"state": "closed", "state_reason": "completed"}
    # Only close if confirmed to be in test repo
    if owner == REPO_OWNER and repo == REPO_NAME:
        response = requests.patch(url, headers=headers, json=data)
        return response.json()
    return None

if __name__ == "__main__":
    print("Automation script for closing issues labeled completed or wontfix")
    print("This script is designed for educational testing in auto-issue-close repository")
    # Example usage would require GITHUB_TOKEN env var
    # For GitHub Actions, see .github/workflows/auto-close.yml
