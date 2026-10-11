import os
import requests

# Script to automatically close issues labeled as completed or wontfix
CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

def close_issue(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    resp = requests.patch(url, json={"state": "closed"}, headers=headers)
    resp.raise_for_status()
    return resp.json()

def list_open_issues(owner, repo, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    resp = requests.get(url, params={"state": "open"}, headers=headers)
    resp.raise_for_status()
    return resp.json()

def main():
    owner = os.environ.get("REPO_OWNER", "karthikabinav")
    repo = os.environ.get("REPO_NAME", "auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    print(f"Checking open issues in {owner}/{repo} for labels: {sorted(CLOSE_LABELS)}")
    if not token:
        print("GITHUB_TOKEN not set; listing logic only (no issues will be closed).")
        return
    for issue in list_open_issues(owner, repo, token):
        if "pull_request" in issue:
            continue
        labels = [label["name"] for label in issue.get("labels", [])]
        if should_close(labels):
            print(f"Closing issue #{issue[number]}: {issue[title]} (labels: {labels})")
            close_issue(owner, repo, issue["number"], token)

if __name__ == "__main__":
    main()
