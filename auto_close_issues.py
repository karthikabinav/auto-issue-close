"""
Automation script to close GitHub issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_for_repo(owner, repo, token=None):
    """
    Example automation logic using GitHub REST API.
    In production, this would list open issues and close those with matching labels.
    """
    # Placeholder for actual API calls - see GitHub Actions workflow for live version
    print(f"Checking open issues in {owner}/{repo} for labels {AUTO_CLOSE_LABELS}...")
    # Pseudo-code:
    # issues = list_open_issues(owner, repo)
    # for issue in issues:
    #     if should_close_issue(issue["labels"]):
    #         close_issue(owner, repo, issue["number"])
    #         print(f"Closed issue #{issue[number]}: {issue[title]}")

if __name__ == "__main__":
    owner = os.getenv("GITHUB_REPOSITORY_OWNER", "karthikabinav")
    repo = os.getenv("GITHUB_REPOSITORY_NAME", "auto-issue-close")
    close_issues_for_repo(owner, repo)
