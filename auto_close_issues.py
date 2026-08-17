"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix
"""
import os
import requests

REPO_OWNER = os.getenv("REPO_OWNER", "karthikabinav")
REPO_NAME = os.getenv("REPO_NAME", "auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
LABELS_TO_CLOSE = {"completed", "wontfix"}

def get_open_issues():
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    params = {"state": "open", "per_page": 100}
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()

def close_issue(issue_number):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}"
    headers = {}
    if GITHUB_TOKEN:
        headers["Authorization"] = f"token {GITHUB_TOKEN}"
    data = {"state": "closed"}
    response = requests.patch(url, headers=headers, json=data)
    response.raise_for_status()
    print(f"Closed issue #{issue_number}")
    # Add comment
    comment_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}/comments"
    comment_data = {"body": "This issue was automatically closed because it is labeled as completed or wontfix."}
    requests.post(comment_url, headers=headers, json=comment_data)

def main():
    issues = get_open_issues()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            print(f"Found issue #{issue[number]} with labels {labels} -> closing")
            try:
                close_issue(issue["number"])
            except Exception as e:
                print(f"Failed to close #{issue[number]}: {e}")
        else:
            print(f"Skipping issue #{issue[number]} labels={labels}")

if __name__ == "__main__":
    main()
