import os
import requests

OWNER = "karthikabinav"
REPO = "auto-issue-close"
CLOSE_LABELS = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"} if token else {}
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            number = issue["number"]
            close_url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{number}"
            requests.patch(close_url, json={"state": "closed"}, headers=headers)
            print(number)

if __name__ == "__main__":
    main()
