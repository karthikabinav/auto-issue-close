import os
from github import Github

# This script automatically closes issues labeled as completed or wontfix
# Requires GITHUB_TOKEN env var and PyGithub

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    g = Github(token) if token else Github()
    repo = g.get_repo(repo_name)
    
    for issue in repo.get_issues(state="open"):
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment("This issue has been automatically closed because it was labeled as completed or wontfix.")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
