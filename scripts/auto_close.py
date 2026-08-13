import os, requests

TOKEN = os.getenv("GITHUB_TOKEN")
owner = "karthikabinav"
repo = "auto-issue-close"
url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
h = {"Authorization": f"token {TOKEN}"}
r = requests.get(url, headers=h).json()
for i in r:
    if "pull_request" in i: continue
    labs = [l["name"] for l in i["labels"]]
    if "completed" in labs or "wontfix" in labs:
        requests.patch(f"https://api.github.com/repos/{owner}/{repo}/issues/{i["number"]}", headers=h, json={"state":"closed"})
        print(f"Closed #{i["number"]}")
