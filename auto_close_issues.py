"""Close open issues labeled `completed` or `wontfix`.

This is a learning example. Provide GITHUB_TOKEN and GITHUB_REPOSITORY
(full repo name such as owner/repo) as environment variables.
"""
import os
import sys
import requests

TARGET_LABELS = {"completed", "wontfix"}


def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo:
        print("Set GITHUB_TOKEN and GITHUB_REPOSITORY.")
        sys.exit(1)
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github+json"}
    page = 1
    while True:
        response = requests.get(
            f"https://api.github.com/repos/{repo}/issues",
            headers=headers,
            params={"state": "open", "page": page},
            timeout=30,
        )
        response.raise_for_status()
        issues = response.json()
        if not issues:
            break
        for issue in issues:
            if issue.get("pull_request"):
                continue
            labels = {label.get("name") for label in issue.get("labels", [])}
            if labels & TARGET_LABELS:
                close = requests.patch(
                    f"https://api.github.com/repos/{repo}/issues/{issue[number]}",
                    headers=headers,
                    json={"state": "closed"},
                    timeout=30,
                )
                close.raise_for_status()
                print(f"Closed #{issue[number]}: {issue.get(title)}")
        page += 1


if __name__ == "__main__":
    main()
