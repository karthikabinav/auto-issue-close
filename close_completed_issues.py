# Script to automatically close issues labeled as completed or wontfix
# Uses the GitHub API via PyGithub if available, otherwise describes the workflow logic.
TARGET_LABELS = {'completed', 'wontfix'}

def should_close(issue):
    labels = {label.name for label in issue.labels}
    return bool(labels & TARGET_LABELS)

def close_labeled_issues(repo):
    closed = []
    for issue in repo.get_issues(state='open'):
        if should_close(issue):
            issue.edit(state='closed')
            closed.append(issue.number)
            print(f'Closed issue #{issue.number}: {issue.title}')
    return closed

if __name__ == '__main__':
    import os
    from github import Github
    token = os.environ.get('GITHUB_TOKEN')
    repo_name = os.environ.get('GITHUB_REPOSITORY', 'karthikabinav/auto-issue-close')
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    close_labeled_issues(repo)
