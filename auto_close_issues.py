"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_for_repo(owner, repo):
    """
    Pseudo-implementation using GitHub API:
    - List open issues
    - For each issue with label completed or wontfix, close it
    """
    print(f"Checking open issues in {owner}/{repo} for labels {AUTO_CLOSE_LABELS}...")
    # Example with PyGithub (to be used in workflow):
    # from github import Github
    # g = Github(os.environ["GITHUB_TOKEN"])
    # r = g.get_repo(f"{owner}/{repo}")
    # for issue in r.get_issues(state="open"):
    #     if should_close_issue([l.name for l in issue.labels]):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    owner = os.environ.get("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo = os.environ.get("GITHUB_REPOSITORY_NAME", "auto-issue-close")
    close_issues_for_repo(owner, repo)
