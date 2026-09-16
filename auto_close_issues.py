#!/usr/bin/env python3
# Automatically closes issues labeled completed or wontfix
import os, requests
REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
LABELS = {"completed", "wontfix"}
owner, repo = REPO.split("/")
headers = {"Authorization": "token " + TOKEN}
issues = requests.get("https://api.github.com/repos/" + owner + "/" + repo + "/issues?state=open", headers=headers).json()
for i in issues:
    names = [l["name"] for l in i["labels"]]
    if any(n in LABELS for n in names):
        requests.patch("https://api.github.com/repos/" + owner + "/" + repo + "/issues/" + str(i["number"]), headers=headers, json={"state": "closed"})
