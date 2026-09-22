#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os, requests
LABELS_TO_CLOSE = {"completed", "wontfix"}
def main():
    owner = os.environ.get("GITHUB_OWNER")
    repo = os.environ.get("GITHUB_REPO", "auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"} if token else {}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    for issue in requests.get(url, headers=headers).json():
        if "pull_request" in issue: continue
        labels = {l.get("name") for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{owner}/{repo}/issues/{issue["number"]}", headers=headers, json={"state": "closed"})
if __name__ == "__main__":
    main()
