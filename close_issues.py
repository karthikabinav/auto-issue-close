import os
from github import Github

LABELS_TO_CLOSE = ["completed", "wontfix"]

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = [l.name for l in issue.labels]
        if any(label in LABELS_TO_CLOSE for label in labels):
            issue.edit(state="closed")
            print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
