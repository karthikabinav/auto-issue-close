"""
Automation script to close GitHub issues labeled as 'completed' or 'wontfix'.

Usage: Set GITHUB_TOKEN and run with owner/repo arguments or adapt for Actions.
"""
import os
import sys

try:
    from github import Github
-except ImportError:
    Github = None

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    label_names = {l.name if hasattr(l, "name") else l for l in issue_labels}
    return bool(label_names & TARGET_LABELS)

def close_labeled_issues(repo):
    closed = []
    for issue in repo.get_issues(state="open"):
        labels = [l.name for l in issue.labels]
        if set(labels) & TARGET_LABELS:
            issue.create_comment("Automatically closing this issue as it was labeled as completed or wontfix.")
            issue.edit(state="closed")
            closed.append(issue.number)
            print(f"Closed issue #{issue.number}: {issue.title} labels={labels}")
    return closed

if __name__ == "__main__":
    if len(sys.argv) == 3:
        owner, repo_name = sys.argv[1], sys.argv[2]
    else:
        repo_full = os.getenv("GITHUB_REPOSITORY", "")
        if "/" not in repo_full:
            print("Usage: python auto_close_issues.py <owner> <repo> or set GITHUB_REPOSITORY")
            sys.exit(1)
        owner, repo_name = repo_full.split("/", 1)
    token = os.getenv("GITHUB_TOKEN")
    if not token or Github is None:
        print("Dry-run mode: logic for closing issues with labels", TARGET_LABELS)
        print(f"Would process repo {owner}/{repo_name}")
    else:
        g = Github(token)
        repo = g.get_repo(f"{owner}/{repo_name}")
        close_labeled_issues(repo)
