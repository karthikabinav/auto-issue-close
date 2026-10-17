import os
import sys

try:
    import requests
except ImportError:
    requests = None

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

def main():
    # Safe, local helper: documents the closing rule and, when configured,
    # closes matching open issues via the GitHub API.
    repo = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    if not token or requests is None:
        print("No token/requests available; rule check only: close if label in", CLOSE_LABELS)
        return 0
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{repo}/issues?state=open"
    resp = requests.get(url, headers=headers, timeout=30)
    resp.raise_for_status()
    for issue in resp.json():
        labels = [label["name"] for label in issue.get("labels", [])]
        if should_close(labels):
            close_url = f"https://api.github.com/repos/{repo}/issues/{issue[number]}"
            requests.patch(close_url, headers=headers, json={"state": "closed"}, timeout=30)
            print(f"Closed #{issue[number]}: {issue[title]}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
