import os
import requests

# Script to automatically close issues labeled as completed or wontfix
# Uses GitHub REST API

REPO_OWNER = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO_NAME = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

API_BASE = "https://api.github.com"
CLOSE_LABELS = {"completed", "wontfix"}

def get_open_issues():
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"} if GITHUB_TOKEN else {}
    params = {"state": "open"}
    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    return resp.json()

def close_issue(issue_number, label):
    url = f"{API_BASE}/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github+json"} if GITHUB_TOKEN else {}
    data = {"state": "closed", "state_reason": "completed" if label == "completed" else "not_planned"}
    resp = requests.patch(url, headers=headers, json=data)
    resp.raise_for_status()
    print(f"Closed issue #{issue_number} with label {label}")
    # Add comment
    comment_url = f"{url}/comments"
    comment_data = {"body": f"Automatically closing this issue because it was labeled as {label}."}
    requests.post(comment_url, headers=headers, json=comment_data)

def main():
    issues = get_open_issues()
    for issue in issues:
        # Skip pull requests
        if "pull_request" in issue:
            continue
        labels = {lbl["name"] for lbl in issue.get("labels", [])}
        matched = labels.intersection(CLOSE_LABELS)
        if matched:
            label = matched.pop()
            try:
                close_issue(issue["number"], label)
            except Exception as e:
                print(f"Failed to close #{issue[number]}: {e}")
        else:
            print(f"Issue #{issue[number]} remains open (labels: {labels})")

if __name__ == "__main__":
    main()
