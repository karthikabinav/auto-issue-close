import os, requests

REPO_OWNER = os.getenv("REPO_OWNER", "karthikabinav")
REPO_NAME = os.getenv("REPO_NAME", "auto-issue-close")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

TARGET_LABELS = {"completed", "wontfix"}

def main():
    headers = {"Authorization": "token " + GITHUB_TOKEN, "Accept": "application/vnd.github+json"}
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open"
    issues = requests.get(url, headers=headers).json()
    for issue in issues:
        if "pull_request" in issue:
            continue
        labels = {l["name"] for l in issue["labels"]}
        if labels & TARGET_LABELS:
            num = issue["number"]
            close_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{num}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})
            comment_url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{num}/comments"
            label = list(labels & TARGET_LABELS)[0]
            requests.post(comment_url, headers=headers, json={"body": f"Auto-closed (label: {label})"})
            print(f"Closed #{num}")

if __name__ == "__main__":
    main()
