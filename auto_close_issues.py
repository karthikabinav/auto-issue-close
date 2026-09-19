#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, requests
OWNER = os.getenv("GITHUB_OWNER", "karthikabinav")
REPO = os.getenv("GITHUB_REPO", "auto-issue-close")
TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}
def main():
    headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}
    resp = requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/issues", headers=headers, params={"state": "open"})
    resp.raise_for_status()
    for issue in resp.json():
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}: {issue["title"]}")
if __name__ == "__main__":
    main()
