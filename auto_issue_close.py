"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")  # owner/repo
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    issues = requests.get(f"https://api.github.com/repos/{repo}/issues?state=open", headers=headers, timeout=30).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{repo}/issues/{issue[chr(39)+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"}, timeout=30)
            print(f"Closed issue #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
