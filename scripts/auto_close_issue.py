import os
import requests

GITHUB_TOKEN = os.getenv(GITHUB_TOKEN)
GITHUB_REPOSITORY = os.getenv(GITHUB_REPOSITORY)
ISSUE_NUMBER = os.getenv(ISSUE_NUMBER)
ISSUE_LABELS = os.getenv(ISSUE_LABELS, ).split(,)

CLOSABLE_LABELS = {completed, wontfix}

def should_close(labels):
    return any(label in CLOSABLE_LABELS for label in labels)

if should_close(ISSUE_LABELS):
    owner, repo = GITHUB_REPOSITORY.split(/)
    url = fhttps://api.github.com/repos/{owner}/{repo}/issues/{ISSUE_NUMBER}
    headers = {Authorization: ftoken {GITHUB_TOKEN}, Accept: application/vnd.github+json}
    data = {state: closed}
    r = requests.patch(url, json=data, headers=headers)
    r.raise_for_status()
    print(fClosed issue #{ISSUE_NUMBER} with labels {ISSUE_LABELS})
else:
    print(fIssue #{ISSUE_NUMBER} not closed, labels: {ISSUE_LABELS})
