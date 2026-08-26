#!/usr/bin/env python3
"""
Automated Issue Closing script.

Closes issues labeled as 'completed' or 'wontfix' in this repository.
Intended to be run via GitHub Actions (see .github/workflows/auto-close-issues.yml)
or manually with a GITHUB_TOKEN environment variable.
"""
import os
import sys

try:
    import requests
except ImportError:
    requests = None

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if not token:
        print("GITHUB_TOKEN not set; this script is designed to run in GitHub Actions.")
        print(f"Would close open issues in {repo} labeled: {sorted(LABELS_TO_CLOSE)}")
        return 0
    if requests is None:
        print("requests library required")
        return 1
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    # List open issues
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels.intersection(LABELS_TO_CLOSE):
            number = issue["number"]
            print(f"Closing issue #{number} labels={labels}")
            # Comment
            requests.post(f"https://api.github.com/repos/{repo}/issues/{number}/comments", headers=headers, json={"body": "Automatically closing this issue as it was labeled as completed or wontfix."}, timeout=30)
            # Close
            requests.patch(f"https://api.github.com/repos/{repo}/issues/{number}", headers=headers, json={"state": "closed"}, timeout=30)
    return 0

if __name__ == "__main__":
    sys.exit(main())
