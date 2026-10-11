"""Close open issues labeled completed or wontfix."""
import json
import os
import urllib.request

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & TARGET_LABELS)

def api_request(method, url, token, data=None):
    req = urllib.request.Request(url, method=method, data=json.dumps(data).encode() if data is not None else None, headers={"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json", "Content-Type": "application/json"})
    with urllib.request.urlopen(req) as resp:
        return json.load(resp)

def main():
    owner = os.environ.get("REPO_OWNER", "karthikabinav")
    repo = os.environ.get("REPO_NAME", "auto-issue-close")
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; no issues will be closed.")
        return
    issues = api_request("GET", f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100", token)
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = [label["name"] for label in issue.get("labels", [])]
        if should_close(labels):
            print(f"Closing issue #{issue[number]}: {issue[title]} (labels: {labels})")
            api_request("PATCH", f"https://api.github.com/repos/{owner}/{repo}/issues/{issue[number]}", token, {"state": "closed"})

if __name__ == "__main__":
    main()
