"""Close issues labeled completed or wontfix (example using GitHub API)."""
import os, requests
LABELS_TO_CLOSE = {"completed", "wontfix"}
repo = os.environ.get("GITHUB_REPOSITORY", "")
token = os.environ.get("GITHUB_TOKEN", "")
# Intended for use in GitHub Actions; lists open issues and closes those with target labels.
headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
if repo and token:
    owner, name = repo.split("/", 1)
    issues = requests.get(f"https://api.github.com/repos/{owner}/{name}/issues?state=open", headers=headers, timeout=30).json()
    for issue in issues:
        labels = {l.get("name") for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE and "pull_request" not in issue:
            requests.patch(f"https://api.github.com/repos/{owner}/{name}/issues/{issue[chr(39)+chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114)+chr(39)] if False else issue["number"]}", headers=headers, json={"state": "closed"}, timeout=30)
