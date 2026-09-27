import os
from github import Github

# Script to automatically close issues labeled as "completed" or "wontfix"
# Usage: set GITHUB_TOKEN and GITHUB_REPOSITORY env vars

def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_name:
        print("Missing GITHUB_TOKEN or GITHUB_REPOSITORY")
        return
    g = Github(token)
    repo = g.get_repo(repo_name)
    target_labels = {"completed", "wontfix"}
    for issue in repo.get_issues(state="open"):
        labels = {l.name for l in issue.labels}
        if labels & target_labels:
            print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
