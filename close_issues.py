"""Script to automatically close issues labeled completed or wontfix."""
import json
import os
import urllib.request

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

def close_issue(owner, repo, issue_number, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
    data = json.dumps({"state": "closed"}).encode()
    req = urllib.request.Request(url, data=data, method="PATCH")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    with urllib.request.urlopen(req) as resp:
        return resp.status

if __name__ == "__main__":
    print("Close issues with labels: completed or wontfix")
