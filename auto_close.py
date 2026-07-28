#!/usr/bin/env python3
"""
Automated Issue Closing Script

This script automatically closes GitHub issues labeled as 'completed' or 'wontfix'.
Designed for learning GitHub automation.

Usage:
  - Set GITHUB_TOKEN environment variable
  - Run: python auto_close.py --repo owner/repo
  - Or use as GitHub Action workflow (see .github/workflows/auto-close.yml)
"""

import os
import sys
import argparse

# Try to import requests, fallback if not available
try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue should be closed based on labels."""
    if not labels:
        return False
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & TARGET_LABELS)

def close_issue_github_api(owner, repo, issue_number, token, reason_label=None):
    """Close a single issue via GitHub API."""
    if not HAS_REQUESTS:
        print("requests library not available, skipping API call")
        return False
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"state": "closed", "state_reason": "completed"}
    resp = requests.patch(url, headers=headers, json=data)
    if resp.status_code == 200:
        print(f"Closed issue #{issue_number} (label: {reason_label})")
        # Add comment
        comment_url = f"{url}/comments"
        comment_body = f"Automatically closed because label `{reason_label}` is in {sorted(TARGET_LABELS)}."
        requests.post(comment_url, headers=headers, json={"body": comment_body})
        return True
    else:
        print(f"Failed to close #{issue_number}: {resp.status_code} {resp.text}")
        return False

def process_repository(owner, repo, token):
    """Process all open issues in repository and close matching ones."""
    if not HAS_REQUESTS:
        print("Simulated run (no requests): would close issues labeled completed/wontfix")
        return
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    resp = requests.get(url, headers=headers)
    if resp.status_code != 200:
        print(f"Error fetching issues: {resp.status_code} {resp.text}")
        return
    issues = resp.json()
    closed_count = 0
    for issue in issues:
        # Ignore pull requests
        if "pull_request" in issue:
            continue
        labels = issue.get("labels", [])
        if should_close_issue(labels):
            label_name = next((l["name"] for l in labels if l["name"] in TARGET_LABELS), "unknown")
            if close_issue_github_api(owner, repo, issue["number"], token, label_name):
                closed_count += 1
    print(f"Done. Closed {closed_count} issue(s).")

def main():
    parser = argparse.ArgumentParser(description="Auto-close issues labeled completed/wontfix")
    parser.add_argument("--repo", required=False, help="Repository in owner/repo format, e.g. karthikabinav/auto-issue-close")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without closing")
    args = parser.parse_args()

    repo_str = args.repo or os.getenv("GITHUB_REPOSITORY")
    token = os.getenv("GITHUB_TOKEN")

    if not repo_str:
        print("No repository specified. Use --repo or GITHUB_REPOSITORY env.")
        print("Example for local testing with mock data:")
        # Demo logic for learning
        sample_issues = [
            {"number": 1, "title": "Implement new feature", "labels": [{"name": "completed"}]},
            {"number": 2, "title": "Remove legacy code", "labels": [{"name": "wontfix"}]},
            {"number": 3, "title": "Fix login error", "labels": [{"name": "bug"}]},
        ]
        for iss in sample_issues:
            action = "CLOSE" if should_close_issue(iss["labels"]) else "KEEP OPEN"
            print(f"Issue #{iss['number']}: '{iss['title']}' labels={[l['name'] for l in iss['labels']]} -> {action}")
        return

    if "/" not in repo_str:
        print(f"Invalid repo format: {repo_str}")
        sys.exit(1)
    owner, repo = repo_str.split("/", 1)

    if args.dry_run:
        print(f"[DRY RUN] Would process {owner}/{repo}")
        # Use token check skipped
        return

    if not token:
        print("GITHUB_TOKEN not set, running in demo mode")
        main_demo = True
        # still show logic
        process_repository(owner, repo, "dummy")
    else:
        process_repository(owner, repo, token)

if __name__ == "__main__":
    main()
