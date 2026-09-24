"""Automatically close issues labeled completed or wontfix."""
import os, requests
REPO = os.environ.get("GITHUB_REPOSITORY")
TOKEN = os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}
headers = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
issues = requests.get(f"https://api.github.com/repos/{REPO}/issues?state=open", headers=headers).json()
for issue in issues:
    labels = {l["name"] for l in issue.get("labels", [])}
    if labels & LABELS_TO_CLOSE:
        requests.patch(f"https://api.github.com/repos/{REPO}/issues/{issue[chr(39)+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"})
