"""Automatically close issues labeled completed or wontfix.

Uses GITHUB_TOKEN from the environment and the GitHub REST API.
Only closes open issues in this repository that carry those labels.
"""
import os, sys, json, urllib.request

LABELS_TO_CLOSE = {"completed", "wontfix"}

def api(method, url, token, data=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(data).encode() if data else None, headers={"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read() or b"{}")

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        sys.exit("GITHUB_TOKEN and GITHUB_REPOSITORY are required")
    issues = api("GET", f"https://api.github.com/repos/{repo}/issues?state=open&per_page=100", token)
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            api("PATCH", f"https://api.github.com/repos/{repo}/issues/{issue[chr(39)+chr(39)] if False else issue["number"]}", token, {"state": "closed"})
            print(f"Closed #{issue["number"]}: {issue["title"]}")

if __name__ == "__main__":
    main()
