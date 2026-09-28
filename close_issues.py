"""
Auto-close GitHub issues labeled completed or wontfix.

Usage:
    GITHUB_TOKEN=ghp_... GITHUB_REPOSITORY=owner/repo python close_issues.py
"""
import os
import sys

import requests

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPOSITORY = os.environ.get("GITHUB_REPOSITORY")
CLOSE_LABELS = {"completed", "wontfix"}

API = "https://api.github.com"


def main() -> None:
    if not GITHUB_TOKEN or not GITHUB_REPOSITORY:
        print("Error: GITHUB_TOKEN and GITHUB_REPOSITORY env vars are required.", file=sys.stderr)
        sys.exit(1)

    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json",
    }

    resp = requests.get(f"{API}/repos/{GITHUB_REPOSITORY}/issues?state=open", headers=headers)
    resp.raise_for_status()

    closed = 0
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            issue_number = issue["number"]
            requests.patch(
                f"{API}/repos/{GITHUB_REPOSITORY}/issues/{issue_number}",
                headers=headers,
                json={"state": "closed"},
            ).raise_for_status()
            print(f"Closed issue #{issue_number} ({issue[title]}) with labels: {sorted(labels & CLOSE_LABELS)}")
            closed += 1

    print(f"Done. Closed {closed} issue(s).")


if __name__ == "__main__":
    main()
