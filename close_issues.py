import os
import requests

# GitHub automation script to close issues labeled "completed" or "wontfix"

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = "karthikabinav/auto-issue-close"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

def close_labeled_issues():
    """Fetch open issues and close those labeled completed or wontfix"""
    url = f"https://api.github.com/repos/{REPO}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=HEADERS)
    issues = resp.json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = [label["name"] for label in issue["labels"]]
        if any(l in ["completed", "wontfix"] for l in labels):
            issue_num = issue["number"]
            close_url = f"https://api.github.com/repos/{REPO}/issues/{issue_num}"
            requests.patch(close_url, headers=HEADERS, json={"state": "closed"})
            comment_url = f"https://api.github.com/repos/{REPO}/issues/{issue_num}/comments"
            requests.post(comment_url, headers=HEADERS, json={"body": "This issue has been automatically closed because it was labeled as completed or wontfix."})
            print(f"Closed issue #{issue_num}")

if __name__ == "__main__":
    close_labeled_issues()
