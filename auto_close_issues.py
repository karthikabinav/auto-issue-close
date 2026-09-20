"""Close issues labeled completed or wontfix via GitHub API."""
import os, requests
OWNER=os.getenv("GITHUB_REPOSITORY_OWNER")
REPO=os.getenv("GITHUB_REPOSITORY", "").split("/")[-1]
TOKEN=os.getenv("GITHUB_TOKEN")
LABELS={"completed", "wontfix"}
headers={"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"}
issues=requests.get(f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open", headers=headers).json()
for issue in issues:
    labels={l["name"] for l in issue.get("labels", [])}
    if labels & LABELS:
        requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(39)+"number"+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"})
