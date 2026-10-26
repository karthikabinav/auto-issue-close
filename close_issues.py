"""Close issues labeled completed or wontfix.

Reads GITHUB_TOKEN and GITHUB_REPOSITORY from environment.
Closes open issues whose labels include 'completed' or 'wontfix'.
"""
import os, requests
REPO=os.environ["GITHUB_REPOSITORY"]
TOKEN=os.environ["GITHUB_TOKEN"]
H={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
for label in ("completed", "wontfix"):
    r=requests.get(f"https://api.github.com/repos/{REPO}/issues", headers=H, params={"state":"open", "labels":label}, timeout=30)
    r.raise_for_status()
    for i in r.json():
        requests.patch(f"https://api.github.com/repos/{REPO}/issues/{i['number']}", headers=H, json={"state":"closed", "state_reason":"completed"}, timeout=30).raise_for_status()
