"""
Automated Issue Closing script for learning GitHub automation.

This script lists open issues in the repository and closes any issue
labeled as completed or wontfix. It leaves other issues (e.g. bug) open.

Usage:
  export GITHUB_TOKEN="<personal-access-token with repo scope>"
  export GITHUB_REPOSITORY="<owner>/<repo>"  # e.g. karthikabinav/auto-issue-close
  python auto_close_issues.py
"""
import os
import sys
import json
import urllib.request
import urllib.error

TARGET_LABELS = {"completed", "wontfix"}

def get_env(name):
    value = os.environ.get(name)
    if not value:
        print(f"Missing required environment variable: {name}", file=sys.stderr)
        sys.exit(1)
    return value

def github_request(method, url, token, data=None):
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "auto-issue-close-student-script"
    }
    body = None
    if data is not None:
        body = json.dumps(data).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    with urllib.request.urlopen(req) as resp:
        return resp.status, json.loads(resp.read().decode("utf-8"))

def main():
    token = get_env("GITHUB_TOKEN")
    repo_full = get_env("GITHUB_REPOSITORY")
    owner, repo = repo_full.split("/", 1)
    list_url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"
    status, issues = github_request("GET", list_url, token)
    for issue in issues:
        if "pull_request" in issue:
            continue
        number = issue["number"]
        title = issue["title"]
        label_names = [lbl["name"] for lbl in issue.get("labels", [])]
        if TARGET_LABELS.intersection(label_names):
            update_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}"
            github_request("PATCH", update_url, token, {"state": "closed"})
            print(f"Closed #{number}: {title}")
        else:
            print(f"Leaving open #{number}: {title}")
    print("Done.")

if __name__ == "__main__":
    main()
