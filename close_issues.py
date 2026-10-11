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

def main():
    owner = os.environ.get("REPO_OWNER", "karthikabinav")
    repo = os.environ.get("REPO_NAME", "auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    # Example: in a real workflow, fetch open issues and close those labeled completed/wontfix
    print(f"Checking open issues in {owner}/{repo} for labels: {sorted(CLOSE_LABELS)}")
    # Logic: for each open issue, if should_close(issue labels): close_issue(...)

if __name__ == "__main__":
    main()
