#!/usr/bin/env python3
import os, requests
REPO=os.environ.get("GITHUB_REPOSITORY")
TOKEN=os.environ.get("GITHUB_TOKEN")
CLOSE_LABELS={"completed","wontfix"}
def main():
    h={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
    base=f"https://api.github.com/repos/{REPO}/issues"
    issues=requests.get(base, headers=h, params={"state":"open"}).json()
    for issue in issues:
        labels={label["name"] for label in issue.get("labels",[])}
        if labels.intersection(CLOSE_LABELS):
            number=issue["number"]
            requests.patch(base+"/"+str(number), headers=h, json={"state":"closed"})
if __name__=="__main__":
    main()
