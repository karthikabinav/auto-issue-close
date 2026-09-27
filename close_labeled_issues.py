"""Automatically close issues labeled "completed" or "wontfix".

This script scans all open issues in a repository and closes any that
carry the "completed" or "wontfix" label. It uses only the Python
standard library, so no extra dependencies are required.

Usage:
    GITHUB_TOKEN=<token> python3 close_labeled_issues.py <owner> <repo>
"""

import json
import os
import sys
import urllib.request

# Issues carrying any of these labels will be closed automatically.
CLOSE_LABELS = {"completed", "wontfix"}


def list_open_issues(owner, repo, token):
    """Fetch every open issue in the repository."""
    issues = []
    page = 1
    while True:
        url = (
            f"https://api.github.com/repos/{owner}/{repo}/issues"
            f"?state=open&per_page=100&page={page}"
        )
        request = urllib.request.Request(url, headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
        })
        with urllib.request.urlopen(request) as response:
            batch = json.loads(response.read().decode("utf-8"))
        if not batch:
            break
        issues.extend(batch)
        page += 1
    return issues


def close_issue(owner, repo, token, number):
    """Close a single issue by number."""
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}"
    data = json.dumps({"state": "closed"}).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method="PATCH",
        headers={
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
        },
    )
    with urllib.request.urlopen(request):
        return True


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 close_labeled_issues.py <owner> <repo>")
        sys.exit(1)

    owner, repo = sys.argv[1], sys.argv[2]
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        sys.exit(1)

    closed = 0
    for issue in list_open_issues(owner, repo, token):
        label_names = {label["name"] for label in issue.get("labels", [])}
        if label_names & CLOSE_LABELS:
            close_issue(owner, repo, token, issue["number"])
            closed += 1
            print(f"Closed issue #{issue[number]}: {issue[title]}")

    print(f"Done. Closed {closed} issue(s).")


if __name__ == "__main__":
    main()
