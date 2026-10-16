import os
import requests

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue):
    labels = [label.get("name") if isinstance(label, dict) else label for label in issue.get("labels", [])]
    return any(label in TARGET_LABELS for label in labels)

def close_labeled_issues(owner, repo, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for issue in response.json():
        if "pull_request" in issue:
            continue
        if should_close(issue):
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue[number]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print(f"Closed issue #{issue[number]}: {issue[title]}")

if __name__ == "__main__":
    close_labeled_issues("karthikabinav", "auto-issue-close", os.environ.get("GITHUB_TOKEN", ""))
