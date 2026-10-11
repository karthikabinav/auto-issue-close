#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
import urllib.request
import json

TARGET_LABELS = {"completed", "wontfix"}

def main():
    repo = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN", "")
    owner, name = repo.split("/", 1)
    url = f"https://api.github.com/repos/{owner}/{name}/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req) as resp:
        issues = json.loads(resp.read())
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue[number]}: {issue[title]} (labels: {sorted(labels & TARGET_LABELS)})")
            # In a real run, PATCH the issue state to closed via the GitHub API here.
            # This script documents the logic; the GitHub Actions workflow performs the actual close.

if __name__ == "__main__":
    main()
