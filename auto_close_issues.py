import os, requests
TOKEN=os.environ["GITHUB_TOKEN"]
OWNER="karthikabinav"
REPO="auto-issue-close"
HEADERS={"Authorization": "Bearer "+TOKEN}
TARGET={"completed", "wontfix"}
for i in requests.get("https://api.github.com/repos/"+OWNER+"/"+REPO+"/issues?state=open", headers=HEADERS).json():
    labels={x["name"] for x in i.get("labels",[])}
    if labels & TARGET:
        requests.patch("https://api.github.com/repos/"+OWNER+"/"+REPO+"/issues/"+str(i["number"]), headers=HEADERS, json={"state":"closed"})
