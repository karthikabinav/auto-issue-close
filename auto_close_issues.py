"""Automatically close issues labeled as completed or wontfix."""
import os, sys, requests
LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    owner = sys.argv[1] if len(sys.argv) > 1 else "karthikabinav"
    repo = sys.argv[2] if len(sys.argv) > 2 else "auto-issue-close"
    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"} if token else {}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues"
    issues = requests.get(url, headers=headers, params={"state": "open", "per_page": 100}).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            requests.patch(f"{url}/{issue[\"number\"]}", headers=headers, json={"state": "closed"})
            print(f"Closed #{issue[\"number\"]}: {issue[\"title\"]}")

if __name__ == "__main__":
    main()
