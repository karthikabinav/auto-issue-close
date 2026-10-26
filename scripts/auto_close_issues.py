#!/usr/bin/env python3
"""
A repository to test GitHub automation for closing labeled issues.
Automatically closes issues labeled as completed or wontfix.
"""
import os
import requests

TOKEN = os.environ.get("GITHUB_TOKEN")
REPO = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{REPO}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        labels = {l["name"].lower() for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            close_url = f"https://api.github.com/repos/{REPO}/issues/{issue[chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)]}"
            # using chr to avoid confusion - number key
            close_url = f"https://api.github.com/repos/{REPO}/issues/{issue["number"]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
