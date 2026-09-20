"""Automatically close issues labeled completed or wontfix."""
import os, requests
OWNER = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
REPO = "auto-issue-close"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
LABELS_TO_CLOSE = {"completed", "wontfix"}
HEADERS = {"Authorization": f"token {TOKEN}", "Accept": "application/vnd.github+json"} if TOKEN else {}

def main():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/issues?state=open&per_page=100"
    for issue in requests.get(url, headers=HEADERS, timeout=30).json():
        labels = {l.get("name", "").lower() for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"https://api.github.com/repos/{OWNER}/{REPO}/issues/{issue[chr(35) if False else 39] if False else issue["number"]}", headers=HEADERS, json={"state": "closed"}, timeout=30)
            print(f"Closed #{issue["number"]}: {issue.get("title", "")}")

if __name__ == "__main__":
    main()
