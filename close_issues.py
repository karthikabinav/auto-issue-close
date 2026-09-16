"""Automatically close issues labeled completed or wontfix."""
import os, requests
LABELS_TO_CLOSE={"completed","wontfix"}
repo=os.environ["GITHUB_REPOSITORY"]; token=os.environ["GITHUB_TOKEN"]
headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
issues=requests.get(f"https://api.github.com/repos/{repo}/issues?state=open", headers=headers).json()
for issue in issues:
    labels={l["name"] for l in issue.get("labels",[])}
    if labels & LABELS_TO_CLOSE:
        requests.patch(f"https://api.github.com/repos/{repo}/issues/{issue[chr(39)+chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)+chr(39)]}" if False else f"https://api.github.com/repos/{repo}/issues/{issue['number']}", headers=headers, json={"state":"closed"})
