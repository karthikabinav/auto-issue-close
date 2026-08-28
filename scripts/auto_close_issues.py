#!/usr/bin/env python3
"""
Automated Issue Closing script
Closes issues labeled as 'completed' or 'wontfix'.
Used for learning GitHub automation. Requires GITHUB_TOKEN env var.
"""
import os
import sys

try:
    import requests
except ImportError:
    requests = None

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if not token:
        print("GITHUB_TOKEN not set; this script is intended to run in GitHub Actions.")
        return 0
    if requests is None:
        print("requests library required")
        return 1
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    owner_repo = repo
    # List open issues
    url = f"https://api.github.com/repos/{owner_repo}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {l["name"].lower() for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            issue_number = issue["number"]
            close_url = f"https://api.github.com/repos/{owner_repo}/issues/{issue_number}"
            r = requests.patch(close_url, headers=headers, json={"state": "closed"})
            r.raise_for_status()
            print(f"Closed issue #{issue_number}: {issue["title"]} labels={labels}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
