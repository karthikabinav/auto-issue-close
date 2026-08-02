import os
from github import Github

# Script to automatically close issues labeled as 'completed' or 'wontfix'
# Usage: python scripts/auto_close.py

REPO = os.getenv('GITHUB_REPOSITORY', 'karthikabinav/auto-issue-close')
TOKEN = os.getenv('GITHUB_TOKEN')

def close_labeled_issues():
    if not TOKEN:
        print('GITHUB_TOKEN not set, skipping')
        return
    g = Github(TOKEN)
    repo = g.get_repo(REPO)
    for issue in repo.get_issues(state='open'):
        labels = [l.name for l in issue.labels]
        if 'completed' in labels or 'wontfix' in labels:
            print(f'Closing issue #{issue.number}: {issue.title} with labels {labels}')
            issue.create_comment(f'Automatically closing issue with labels: {labels}')
            issue.edit(state='closed')

if __name__ == '__main__':
    close_labeled_issues()
