"""
Automated Issue Closing Script
Closes issues labeled as 'completed' or 'wontfix'
"""
import os
from github import Github

# For use with PyGithub - can also be adapted for github MCP tools
REPO_NAME = os.getenv('GITHUB_REPOSITORY', 'karthikabinav/auto-issue-close')
TOKEN = os.getenv('GITHUB_TOKEN')
LABELS_TO_CLOSE = ['completed', 'wontfix']

def close_labeled_issues(repo):
    """Close open issues that have 'completed' or 'wontfix' labels."""
    issues = repo.get_issues(state='open')
    for issue in issues:
        labels = [l.name for l in issue.labels]
        if any(lbl in LABELS_TO_CLOSE for lbl in labels):
            reason = 'completed' if 'completed' in labels else 'not_planned'
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.create_comment(f"Automatically closing this issue because it was labeled as **{labels}**.")
            issue.edit(state='closed', state_reason=reason)

if __name__ == '__main__':
    # Example usage with local token, or designed to run in GitHub Actions
    if TOKEN:
        g = Github(TOKEN)
        repo = g.get_repo(REPO_NAME)
        close_labeled_issues(repo)
    else:
        print("Set GITHUB_TOKEN to run against live repository.")
        print(f"Target repo: {REPO_NAME}")
        print(f"Would close issues with labels: {LABELS_TO_CLOSE}")
