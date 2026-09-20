import os
import requests
repo = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
token = os.getenv("GITHUB_TOKEN")
headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"} if token else {}
close_labels = {"completed", "wontfix"}
issues = requests.get("https://api.github.com/repos/" + repo + "/issues?state=open", headers=headers).json()
for issue in issues:
    labels = set(label["name"] for label in issue.get("labels", []))
    if labels.intersection(close_labels):
        num = issue["number"]
        requests.patch("https://api.github.com/repos/" + repo + "/issues/" + str(num), headers=headers, json={"state": "closed"})
        print("Closed issue", num)
