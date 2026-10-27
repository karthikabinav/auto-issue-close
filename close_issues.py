"""Close specific GitHub issues labeled completed or wontfix.

Safe, targeted automation: it only checks issue numbers explicitly
passed on the command line, so it never performs a repository-wide
sweep. It reads GITHUB_TOKEN and GITHUB_REPOSITORY from the
environment, verifies each target is an open issue (not a pull
request), and closes it only if its labels include completed or
wontfix.

Usage: python close_issues.py <issue_number> [<issue_number> ...]
Example: python close_issues.py 123 124
"""
import os
import sys
import requests

REPO = os.environ["GITHUB_REPOSITORY"]
TOKEN = os.environ["GITHUB_TOKEN"]
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json"}
CLOSE_LABELS = {"completed", "wontfix"}


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Provide at least one issue number; refusing repository-wide sweep.")
    numbers = sorted({int(value) for value in sys.argv[1:]})
    if any(number <= 0 for number in numbers):
        raise SystemExit("Issue numbers must be positive integers.")
    for number in numbers:
        response = requests.get(f"https://api.github.com/repos/{REPO}/issues/{number}", headers=HEADERS, timeout=30)
        response.raise_for_status()
        issue = response.json()
        if "pull_request" in issue or issue.get("state") != "open":
            print(f"Skipping #{number}: not an open issue.")
            continue
        labels = {label.get("name") for label in issue.get("labels", [])}
        if not (labels & CLOSE_LABELS):
            print(f"Leaving #{number} open: labels {sorted(labels)} have no completed/wontfix label.")
            continue
        reason = "completed" if "completed" in labels else "not_planned"
        close = requests.patch(f"https://api.github.com/repos/{REPO}/issues/{number}", headers=HEADERS, json={"state": "closed", "state_reason": reason}, timeout=30)
        close.raise_for_status()
        print(f"Closed #{number} with state_reason={reason}.")


if __name__ == "__main__":
    main()
