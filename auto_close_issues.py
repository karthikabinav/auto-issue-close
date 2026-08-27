"""
Automation script to automatically close issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if any label triggers auto-close."""
    return any(label.lower() in AUTO_CLOSE_LABELS for label in labels)

def close_issues_for_repo(owner, repo):
    """
    Example logic using GitHub API (pseudo-code):
    - List open issues
    - For each issue, if labels contain completed or wontfix, close it
    """
    print(f"Checking open issues in {owner}/{repo} for labels {AUTO_CLOSE_LABELS}...")
    # In real workflow, use PyGithub or REST API:
    # issues = github.list_issues(owner, repo, state="open")
    # for issue in issues:
    #     labels = [l["name"] for l in issue["labels"]]
    #     if should_close(labels):
    #         github.update_issue(owner, repo, issue["number"], state="closed")
    #         print(f"Closed issue #{issue[number]}: {issue[title]}")

if __name__ == "__main__":
    owner = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
    close_issues_for_repo(owner, repo)
