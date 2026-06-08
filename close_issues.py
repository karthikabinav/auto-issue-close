import os
import requests

REPO_OWNER = "karthikabinav"
REPO_NAME = "auto-issue-close"
LABELS_TO_CLOSE = ["completed", "wontfix"]
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

def close_labeled_issues():
    headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    for issue in r.json():
        labels = [lbl["name"] for lbl in issue.get("labels", [])]
        if any(l in LABELS_TO_CLOSE for l in labels):
            close_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue[number]}"
            resp = requests.patch(close_url, headers=headers, json={"state": "closed"})
            if resp.status_code == 200:
                print(f"Closed issue #{issue[number]}: {issue[title]}")

if __name__ == "__main__":
    close_labeled_issues()
