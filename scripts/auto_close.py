"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix
"""
import os
from github import Github

def close_labeled_issues(owner, repo):
    token = os.getenv("GITHUB_TOKEN")
    g = Github(token)
    repository = g.get_repo(f"{owner}/{repo}")
    for label in ["completed", "wontfix"]:
        for issue in repository.get_issues(state="open", labels=[label]):
            print(f"Closing #{issue.number}: {issue.title}")
            issue.edit(state="closed")
            issue.create_comment(f"Auto-closed as \"{label}\".")

if __name__ == "__main__":
    import sys
    o = sys.argv[1] if len(sys.argv)>1 else "karthikabinav"
    r = sys.argv[2] if len(sys.argv)>2 else "auto-issue-close"
    close_labeled_issues(o,r)
