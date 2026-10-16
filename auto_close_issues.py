"""Automatically close issues labeled completed or wontfix."""
import json
import os
import urllib.request
CLOSE_LABELS = {"completed", "wontfix"}
def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)
def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        raise SystemExit("Set GITHUB_TOKEN and GITHUB_REPOSITORY")
    headers = {"Authorization": "token " + token, "Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/" + repo + "/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        issues = json.load(resp)
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = set()
        for label in issue.get("labels", []):
            labels.add(label.get("name"))
        number = issue.get("number")
        title = issue.get("title")
        if should_close(labels):
            print("Closing", number, title, labels)
            data = json.dumps({"state": "closed"}).encode()
            req2 = urllib.request.Request("https://api.github.com/repos/" + repo + "/issues/" + str(number), data=data, headers=headers, method="PATCH")
            with urllib.request.urlopen(req2) as resp2:
                print(resp2.status)
        else:
            print("Leaving open", number, title, labels)
if __name__ == "__main__":
    main()
