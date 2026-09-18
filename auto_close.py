import os
from github import Github

# Script to automatically close issues labeled as completed or wontfix
# Usage: python auto_close.py
REPO = os.getenv('GITHUB_REPOSITORY', 'karthikabinav/auto-issue-close')
TOKEN = os.getenv('GITHUB_TOKEN')

def main():
    g = Github(TOKEN) if TOKEN else Github()
    repo = g.get_repo(REPO)
    for issue in repo.get_issues(state='open'):
        labels = [l.name for l in issue.labels]
        if 'completed' in labels or 'wontfix' in labels:
            print(f'Closing issue #{issue.number}: {issue.title} with labels {labels}')
            # issue.edit(state='closed')

if __name__ == '__main__':
    main()
