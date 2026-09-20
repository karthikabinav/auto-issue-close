"""Close issues labeled completed or wontfix.

Educational example for GitHub automation in this test repository only.
Uses GITHUB_TOKEN from environment, lists open issues, and closes those with labels completed/wontfix.
"""
import os, requests
OWNER=os.getenv("GITHUB_REPOSITORY_OWNER")
REPO=os.getenv("GITHUB_REPOSITORY", "").split("/")[-1]
TOKEN=os.getenv("GITHUB_TOKEN")
LABELS={"completed", "wontfix"}
headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
issues=requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open", headers=headers).json()
for issue in issues:
    if LABELS.intersection({l["name"] for l in issue.get("labels", [])}):
        requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue["number"]}", headers=headers, json={"state": "closed"})
