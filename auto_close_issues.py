#!/usr/bin/env python3
"""Automation script to close issues labeled as completed or wontfix."""
import os
import sys
CLOSE_LABELS = {"completed", "wontfix"}
def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)
def main():
    import requests
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Set GITHUB_TOKEN and GITHUB_REPOSITORY")
        return 1
    headers = {"Authorization": "token " + token, "Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/" + repo + "/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        if "pull_request" in issue:
            continue
        labels = [l.get("name") for l in issue.get("labels", [])]
        number = issue.get("number")
        title = issue.get("title")
        if should_close(labels):
            print("Closing issue", number, title, labels)
            close_url = "https://api.github.com/repos/" + repo + "/issues/" + str(number)
            r = requests.patch(close_url, headers=headers, json={"state": "closed"})
            r.raise_for_status()
        else:
            print("Leaving open issue", number, title, labels)
    return 0
if __name__ == "__main__":
    sys.exit(main())
