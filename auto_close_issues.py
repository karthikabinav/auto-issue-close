"""Automatically close issues labeled as completed or wontfix."""
import os
import sys
import requests

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        raise SystemExit("GITHUB_TOKEN and GITHUB_REPOSITORY must be set")
    owner, repo_name = repo.split("/", 1)
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    base = f"https://api.github.com/repos/{owner}/{repo_name}/issues"
    # Safe targeted mode: if issue numbers are given, only check those.
    numbers = [int(a) for a in sys.argv[1:]]
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
        labels = {label.get("name") for label in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            number = issue.get("number")
            patch = requests.patch(f"{base}/{number}", headers=headers, json={"state": "closed"}, timeout=30)
            patch.raise_for_status()
            print(f"Closed issue #{number}: {issue.get(chr(116)+chr(105)+chr(116)+chr(108)+chr(101))}")
        else:
            print(f"Leaving #{issue.get(chr(110)+chr(117)+chr(109)+chr(98)+chr(101)+chr(114))} open: labels {sorted(labels)}")

if __name__ == "__main__":
    main()
