import os, requests
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ["GITHUB_TOKEN"]
    repo = os.environ["GITHUB_REPOSITORY"]
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/" + repo + "/issues"
    issues = requests.get(url, headers=headers, params={"state": "open"}, timeout=30).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(url + "/" + str(issue["number"]), headers=headers, json={"state": "closed"}, timeout=30)
            print("Closed issue", issue["number"])

if __name__ == "__main__":
    main()
