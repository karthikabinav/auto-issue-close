#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix."""
import os, sys
try:
    from github import Github
except ImportError:
    Github = None
LABELS_TO_CLOSE = {"completed", "wontfix"}
def main():
    token = os.environ.get("GITHUB_TOKEN")
    repo_name = os.environ.get("GITHUB_REPOSITORY")
    if not token or not repo_name or Github is None:
        print("Missing GITHUB_TOKEN/GITHUB_REPOSITORY or PyGithub; workflow github-script handles closing.")
        return
    gh = Github(token)
    repo = gh.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {l.name for l in issue.labels}
        if labels & LABELS_TO_CLOSE:
            issue.edit(state="closed")
            print(f"Closed #{issue.number}: {issue.title}")
if __name__ == "__main__":
    main()
