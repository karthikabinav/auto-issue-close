#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, requests
OWNER=os.getenv("GITHUB_OWNER", "karthikabinav")
REPO=os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN=os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE={"completed", "wontfix"}
HEADERS={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github.v3+json"} if TOKEN else {}

def main():
    url=f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open&per_page=100"
    issues=requests.get(url, headers=HEADERS).json()
    for issue in issues:
        labels={l.get("name") for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}", headers=HEADERS, json={"state": "closed"})
            print(f"Closed #{issue["number"]}: {issue["title"]}")
if __name__=="__main__":
    main()
