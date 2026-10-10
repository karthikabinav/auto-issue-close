#!/usr/bin/env python3
"""
Automation script to close issues labeled as completed or wontfix.
Uses the GitHub REST API via the gh CLI / requests with GITHUB_TOKEN.
Only closes issues with labels completed or wontfix; leaves others (e.g. bug) open.
"""
import os
import sys
try:
    import requests
except ImportError:
    requests = None

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

def main():
    if requests is None:
        print("requests library required")
        return 1
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Set GITHUB_TOKEN and GITHUB_REPOSITORY (owner/repo)")
        return 1
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = [l["name"] for l in issue.get("labels", [])]
        if should_close(labels):
            print(f"Closing issue #{issue[number]}: {issue[title]} labels={labels}")
            close_url = f"https://api.github.com/repos/{repo}/issues/{issue[number]}"
            r = requests.patch(close_url, headers=headers, json={"state": "closed"})
            r.raise_for_status()
        else:
            print(f"Leaving open issue #{issue[number]}: {issue[title]} labels={labels}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
