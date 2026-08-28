"""
Automated Issue Closing Script
Closes GitHub issues labeled as 'completed' or 'wontfix'.
Intended for learning GitHub automation / GitHub Actions.
"""
import os

try:
    from github import Github
except ImportError:
    Github = None

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    token = os.getenv("GITHUB_TOKEN")
    repo_name = os.getenv("GITHUB_REPOSITORY")
    if not token or not repo_name:
        print("Missing GITHUB_TOKEN or GITHUB_REPOSITORY env vars")
        return
    if Github is None:
        print("PyGithub not installed")
        return
    g = Github(token)
    repo = g.get_repo(repo_name)
    for issue in repo.get_issues(state="open"):
        labels = {label.name for label in issue.labels}
        if labels & LABELS_TO_CLOSE:
            print(f"Closing issue #{issue.number}: {issue.title} labels={labels}")
            issue.create_comment("Auto-closed because it is labeled as completed or wontfix.")
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
