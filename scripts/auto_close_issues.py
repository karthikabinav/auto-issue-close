#!/usr/bin/env python3
"""
Automated Issue Closing script.
A repository to test GitHub automation for closing labeled issues.
Closes issues labeled as 'completed' or 'wontfix'.
"""
import os
import sys
import requests

REPO_OWNER = os.environ.get('GITHUB_REPOSITORY_OWNER', 'karthikabinav')
REPO_NAME = os.environ.get('GITHUB_REPOSITORY_NAME', 'auto-issue-close')
TOKEN = os.environ.get('GITHUB_TOKEN')
LABELS_TO_CLOSE = {'completed', 'wontfix'}

def main():
    if not TOKEN:
        print('GITHUB_TOKEN not set')
        sys.exit(1)
    headers = {'Authorization': f'Bearer {TOKEN}', 'Accept': 'application/vnd.github+json'}
    url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues?state=open&per_page=100'
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    for issue in resp.json():
        if 'pull_request' in issue:
            continue
        labels = {l['name'] for l in issue.get('labels', [])}
        matched = labels & LABELS_TO_CLOSE
        if matched:
            label_str = ', '.join(sorted(matched))
            print(f"Closing issue #{issue['number']} labeled {label_str}")
            comment_url = issue['comments_url']
            requests.post(comment_url, headers=headers, json={'body': f'This issue was automatically closed because it was labeled as {label_str}.'})
            issue_url = issue['url']
            requests.patch(issue_url, headers=headers, json={'state': 'closed'})

if __name__ == '__main__':
    main()
