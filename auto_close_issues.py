#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os, requests
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO = "auto-issue-close"
TOKEN = os.environ.get("GITHUB_TOKEN")
CLOSE_LABELS = {"completed", "wontfix"}
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"} if TOKEN else {}
def main():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    issues = requests.get(url, headers=HEADERS).json()
    for issue in issues:
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)+chr(39)] if False else issue["number"]}", headers=HEADERS, json={"state": "closed"})
            print(f"Closed #{issue[chr(39)] if False else issue["number"]}")
if __name__ == "__main__":
    main()
