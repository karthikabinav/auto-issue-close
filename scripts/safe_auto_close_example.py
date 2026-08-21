#!/usr/bin/env python3
"""
Safe auto-close example for GitHub issues.
- Lists issues with labels completed/wontfix
- Logs what WOULD be closed (dry-run by default)
- Requires --confirm flag to actually close
- Never closes issues labeled "bug"
"""
import argparse
import os
import sys
import requests

GITHUB_API = "https://api.github.com"

def list_issues(owner, repo, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues?state=open&per_page=100"
    resp = requests.get(url, headers=headers)
    resp.raise_for_status()
    return resp.json()

def close_issue(owner, repo, issue_number, token):
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github+json"}
    url = f"{GITHUB_API}/repos/{owner}/{repo}/issues/{issue_number}"
    data = {"state": "closed"}
    resp = requests.patch(url, headers=headers, json=data)
    resp.raise_for_status()
    return resp.json()

def main():
    parser = argparse.ArgumentParser(description="Safe auto-close for completed/wontfix")
    parser.add_argument("--owner", default="karthikabinav")
    parser.add_argument("--repo", default="auto-issue-close")
    parser.add_argument("--confirm", action="store_true", help="Actually close issues (default dry-run)")
    args = parser.parse_args()
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Set GITHUB_TOKEN env var")
        sys.exit(1)
    issues = list_issues(args.owner, args.repo, token)
    to_close = []
    for iss in issues:
        labels = [lbl["name"] for lbl in iss.get("labels", [])]
        if "bug" in labels:
            continue
        if "completed" in labels or "wontfix" in labels:
            to_close.append(iss)
    if not to_close:
        print("No issues to close")
        return
    for iss in to_close:
        labels = [lbl["name"] for lbl in iss.get("labels", [])]
        print(f"Issue #{iss[\"number\"]} \"{iss[\"title\"]}\" labels {labels} -> {\"CLOSING\" if args.confirm else \"would close (dry-run)\"}")
        if args.confirm:
            close_issue(args.owner, args.repo, iss["number"], token)
            print(f"Closed #{iss[\"number\"]}")

if __name__ == "__main__":
    main()
