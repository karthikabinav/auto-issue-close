import os
import requests

TARGET_LABELS = {"completed", "wontfix"}
def should_close(issue):
    labels = [label.get("name") if isinstance(label, dict) else label for label in issue.get("labels", [])]
    return any(label in TARGET_LABELS for label in labels)
def close_labeled_issues(owner, repo, token):
    headers = {"Authorization": "token " + token, "Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/" + owner + "/" + repo + "/issues?state=open"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    for issue in response.json():
        if "pull_request" in issue:
            continue
        if should_close(issue):
            close_url = "https://api.github.com/repos/" + owner + "/" + repo + "/issues/" + str(issue["number"])
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            print("Closed issue #" + str(issue["number"]) + ": " + issue["title"])

if __name__ == "__main__":
    close_labeled_issues("karthikabinav", "auto-issue-close", os.environ.get("GITHUB_TOKEN", ""))
