import os
from github import Github

# Script to automatically close issues labeled as completed or wontfix
# Uses PyGithub library

def auto_close_issues(repo_name, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    issues = repo.get_issues(state='open')
    for issue in issues:
        labels = [label.name for label in issue.labels]
        if 'completed' in labels or 'wontfix' in labels:
            print(f"Closing issue #{issue.number}: {issue.title} with labels {labels}")
            issue.create_comment(f"Auto-closing issue with labels: {', '.join(labels)}")
            issue.edit(state='closed')

if __name__ == "__main__":
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
    if not token:
        print("GITHUB_TOKEN not set")
    else:
        auto_close_issues(repo_name, token)
