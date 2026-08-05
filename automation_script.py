import os
import requests

# GitHub Automation Script for closing issues with specific labels
# This script closes issues labeled as completed or wontfix

GITHUB_TOKEN = os.environ.get(GITHUB_TOKEN)
REPO_OWNER = karthikabinav
REPO_NAME = auto-issue-close

HEADERS = {
    Authorization: ftoken {GITHUB_TOKEN},
    Accept: application/vnd.github.v3+json
}

def get_open_issues():
    url = fhttps://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open
    response = requests.get(url, headers=HEADERS)
    return response.json()

def close_issue(issue_number):
    url = fhttps://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues/{issue_number}
    data = {state: closed}
    response = requests.patch(url, headers=HEADERS, json=data)
    return response.json()

def main():
    issues = get_open_issues()
    closed_labels = [completed, wontfix]
    
    for issue in issues:
        if pull_request in issue:
            continue  # Skip PRs
            
        labels = [label[name] for label in issue[labels]]
        if any(label in closed_labels for label in labels):
            print(f"Closing issue #{issue[number]}: {issue[title]}")
            close_issue(issue[number])
            print(f"Successfully closed issue with labels: {labels}")

if __name__ == __main__:
    main()