import os
import requests

# GitHub automation script to close issues labeled as completed or wontfix
# Usage: Set GITHUB_TOKEN and GITHUB_REPOSITORY env vars

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY")  # e.g., owner/repo
API_BASE = "https://api.github.com"

TARGET_LABELS = {"completed", "wontfix"}

def get_open_issues():
    url = f"{API_BASE}/repos/{REPO}/issues?state=open&per_page=100"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    return r.json()

def close_issue(issue_number):
    url = f"{API_BASE}/repos/{REPO}/issues/{issue_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}
    data = {"state": "closed", "state_reason": "completed"}
    r = requests.patch(url, headers=headers, json=data)
    r.raise_for_status()
    print(f"Closed issue #{issue_number}")
    # Add comment
    comment_url = f"{API_BASE}/repos/{REPO}/issues/{issue_number}/comments"
    comment = {"body": f"Automatically closing issue labeled as completed/wontfix."}
    requests.post(comment_url, headers=headers, json=comment)

def main():
    if not GITHUB_TOKEN or not REPO:
        print("Missing GITHUB_TOKEN or GITHUB_REPOSITORY")
        return
    issues = get_open_issues()
    for issue in issues:
        labels = {lbl["name"] for lbl in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            print(f"Issue #{issue[number]} titled \"{issue[title]}\" has labels {labels} -> closing")
            close_issue(issue["number"])

if __name__ == "__main__":
    main()
