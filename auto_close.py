import os
import requests

"""
Automated Issue Closing Script

This script automatically closes GitHub issues labeled as 'completed' or 'wontfix'.
It can be used locally or as part of a GitHub Actions workflow.
"""

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
API_URL = f"https://api.github.com/repos/{REPO}/issues"

HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def should_close(labels):
    label_names = [l["name"].lower() if isinstance(l, dict) else l.lower() for l in labels]
    return "completed" in label_names or "wontfix" in label_names

def close_issues():
    if not GITHUB_TOKEN:
        print("GITHUB_TOKEN not set, running in dry-run mode")
    params = {"state": "open", "per_page": 100}
    r = requests.get(API_URL, headers=HEADERS, params=params)
    r.raise_for_status()
    issues = r.json()
    for issue in issues:
        if should_close(issue.get("labels", [])):
            number = issue["number"]
            print(f"Closing issue #{number}: {issue['title']} with labels {[l['name'] for l in issue['labels']]}")
            if GITHUB_TOKEN:
                close_url = f"https://api.github.com/repos/{REPO}/issues/{number}"
                requests.patch(close_url, headers=HEADERS, json={"state": "closed", "state_reason": "completed"})
                comment_url = close_url + "/comments"
                requests.post(comment_url, headers=HEADERS, json={"body": "🤖 This issue was automatically closed because it has the `completed` or `wontfix` label."})

if __name__ == "__main__":
    close_issues()
