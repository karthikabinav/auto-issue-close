"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# This script is intended to be run via GitHub Actions
# It checks open issues and closes those with completed/wontfix labels

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo_name:
        print("Missing GITHUB_TOKEN or GITHUB_REPOSITORY")
        return
    
    g = Github(token)
    repo = g.get_repo(repo_name)
    
    for issue in repo.get_issues(state="open"):
        labels = [label.name for label in issue.labels]
        if "completed" in labels or "wontfix" in labels:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
