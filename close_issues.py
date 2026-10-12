# Automatically close issues labeled completed or wontfix.
# Usage: set GITHUB_TOKEN and GITHUB_REPOSITORY, then run python close_issues.py
# The script lists open issues and closes any issue with label completed or wontfix.
# Issues with other labels, for example bug, are left open.
import os
import sys
import urllib.request
import json
CLOSE_LABELS = {"completed", "wontfix"}
def api_request(url, token, method="GET", data=None):
    req = urllib.request.Request(url, method=method)
    req.add_header("Authorization", "Bearer " + token)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    body = json.dumps(data).encode() if data is not None else None
    if body is not None:
        req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, data=body) as resp:
        return json.loads(resp.read().decode())
def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Set GITHUB_TOKEN and GITHUB_REPOSITORY environment variables.", file=sys.stderr)
        return 1
    base = "https://api.github.com/repos/" + repo
    issues = api_request(base + "/issues?state=open&per_page=100", token)
    closed = []
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"].lower() for label in issue.get("labels", [])}
        if labels & CLOSE_LABELS:
            api_request(base + "/issues/" + str(issue["number"]), token, method="PATCH", data={"state": "closed"})
            closed.append(issue["number"])
            print("Closed issue #" + str(issue["number"]) + ": " + issue["title"])
    print("Closed " + str(len(closed)) + " issue(s).")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
