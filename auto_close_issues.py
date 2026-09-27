{"""Automatically close GitHub issues labeled completed or wontfix."""}

import json
import os
import urllib.error
import urllib.request

API_BASE = "https://api.github.com"
TARGET_LABELS = {"completed", "wontfix"}


def close_issue(repo, token, issue_number):
    url = f"{API_BASE}/repos/{repo}/issues/{issue_number}"
    payload = json.dumps({"state": "closed"}).encode("utf-8")
    request = urllib.request.Request(url, data=payload, method="PATCH")
    request.add_header("Authorization", f"Bearer {token}")
    request.add_header("Accept", "application/vnd.github+json")
    try:
        with urllib.request.urlopen(request) as response:
            status = response.status
    except urllib.error.HTTPError as error:
        print(f"Failed to close issue #{issue_number}: HTTP {error.code}")
        return False
    if status in {200, 201}:
        print(f"Closed issue #{issue_number}.")
        return True
    print(f"Failed to close issue #{issue_number}: HTTP {status}")
    return False


def process_open_issues(repo, token):
    closed = []
    skipped = []
    page = 1
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
    }
    while True:
        url = f"{API_BASE}/repos/{repo}/issues?state=open&per_page=100&page={page}"
        request = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(request) as response:
            issues = json.loads(response.read().decode("utf-8"))
        if not issues:
            break
        for issue in issues:
            if "pull_request" in issue:
                continue  # Keep pull requests out of this simple issue automation.
            labels = {label.get("name") for label in issue.get("labels", [])}
            if labels & TARGET_LABELS:
                if close_issue(repo, token, issue["number"]):
                    closed.append(issue["number"])
            else:
                skipped.append(issue["number"])
        page += 1
    print(f"Closed {len(closed)} issue(s): {closed}")
    print(f"Left {len(skipped)} other open issue(s) unchanged: {skipped}")
    return closed


if __name__ == "__main__":
    repo = os.environ.get("GITHUB_REPOSITORY")
    token = os.environ.get("GITHUB_TOKEN")
    if not repo or not token:
        raise SystemExit(
            "Set GITHUB_REPOSITORY (for example owner/repo) and GITHUB_TOKEN before running."
        )
    process_open_issues(repo, token)
