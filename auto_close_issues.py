"""Automatically close issues labeled as completed or wontfix."""
import os
import sys
import requests

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if not token:
        print("GITHUB_TOKEN not set; dry-run mode listing target labels", LABELS_TO_CLOSE)
        return
    owner, repo_name = repo.split("/", 1)
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    base = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    numbers = [int(a) for a in sys.argv[1:]] if len(sys.argv) > 1 else []
    if numbers:
        issues = []
        for n in numbers:
            r = requests.get(f"{base}/{n}", headers=headers, timeout=30)
            r.raise_for_status()
            issues.append(r.json())
    else:
        r = requests.get(base, headers=headers, params={"state": "open", "per_page": 100}, timeout=30)
        r.raise_for_status()
        issues = r.json()
    for issue in issues:
        if "pull_request" in issue or issue.get("state") != "open":
            continue
        labels = {label.get("name") if isinstance(label, dict) else label for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            number = issue.get("number")
            patch = requests.patch(f"{base}/{number}", headers=headers, json={"state": "closed"}, timeout=30)
            patch.raise_for_status()
            print(f"Closed issue #{number}")
        else:
            print(f"Leaving #{issue.get("number")} open")

if __name__ == "__main__":
    main()
