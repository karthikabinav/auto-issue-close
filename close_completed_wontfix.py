#!/usr/bin/env python3
"""
Automated Issue Closing Script

This script automatically closes GitHub issues labeled as 'completed' or 'wontfix'.
Designed for GitHub automation workflows.

Usage: Can be integrated into GitHub Actions with:
  on:
    issues:
      types: [labeled]
"""

import os
import requests

def close_labeled_issues():
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set")
        return
    
    owner = "karthikabinav"
    repo = "auto-issue-close"
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    
    # Get open issues
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f"Error fetching issues: {response.status_code}")
        return
    
    issues = response.json()
    target_labels = ["completed", "wontfix"]
    closed_count = 0
    
    for issue in issues:
        if "pull_request" in issue:
            continue
            
        labels = [l["name"].lower() for l in issue["labels"]]
        
        if any(label in labels for label in target_labels):
            issue_number = issue["number"]
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
            
            payload = {"state": "closed"}
            close_resp = requests.patch(close_url, headers=headers, json=payload)
            
            if close_resp.status_code == 200:
                print(f"Closed issue #{issue_number}: {issue[title]}")
                print(f"  Labels: {labels}")
                closed_count += 1
    
    print(f"\nTotal issues closed: {closed_count}")
    print("Automation complete!")

if __name__ == "__main__":
    close_labeled_issues()
