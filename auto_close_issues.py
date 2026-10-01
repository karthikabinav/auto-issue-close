#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix."""
import os
try:
    from github import Github
    client = Github(os.getenv("GITHUB_TOKEN"))
    repo = client.get_repo(os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close"))
    TARGET_LABELS = {"completed", "wontfix"}
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & TARGET_LABELS:
            print(f"Closing issue #{issue.number}: {issue.title} (labels: {labels})")
            issue.edit(state="closed")
except Exception as e:
    print(f"Script requires PyGithub and a GITHUB_TOKEN; logic: close open issues with labels completed or wontfix. Error: {e}")
