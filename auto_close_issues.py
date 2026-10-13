"""
Automated Issue Closing script for learning GitHub automation.

This script lists open issues in the repository and closes any issue
labeled as completed or wontfix. It leaves other issues (e.g. bug) open.

Usage:
  export GITHUB_TOKEN="<personal-access-token with repo scope>"
  export GITHUB_REPOSITORY="<owner>/<repo>"  # e.g. karthikabinav/auto-issue-close
  python auto_close_issues.py

For students: this is a simple example using only the standard library
(urllib) so no extra dependencies are needed.
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
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"GitHub API error {e.code} for {method} {url}: {e.read().decode()}", file=sys.stderr)
        raise

def main():
    token = get_env("GITHUB_TOKEN")
    repo_full = get_env("GITHUB_REPOSITORY")
    try:
        owner, repo = repo_full.split("/", 1)
    except ValueError:
        print("GITHUB_REPOSITORY must be in format owner/repo", file=sys.stderr)
        sys.exit(1)

    list_url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"
    print(f"Listing open issues for {owner}/{repo}...")
    status, issues = github_request("GET", list_url, token)
    print(f"Found {len(issues)} open issue(s)")

    for issue in issues:
        # Skip pull requests (they also appear in issues API)
        if "pull_request" in issue:
            continue
        number = issue["number"]
        title = issue["title"]
        label_names = [lbl["name"] for lbl in issue.get("labels", [])]
        print(f"#{number}: {title} labels={label_names}")
        if TARGET_LABELS.intersection(label_names):
            print(f"  -> Closing #{number} (matched completed/wontfix)")
            update_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}"
            # Optional: leave a comment explaining the automation
            comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments"
            try:
                github_request("POST", comment_url, token, {"body": "Automatically closed by student automation: labeled as `completed` or `wontfix`."})
            except Exception:
                print(f"  warning: could not add comment to #{number}", file=sys.stderr)
            github_request("PATCH", update_url, token, {"state": "closed"})
        else:
            print(f"  -> Leaving #{number} open")
    print("Done.")

if __name__ == "__main__":
    main()
