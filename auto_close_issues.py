"""
Automated Issue Closing Script
Automatically closes issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_example():
    """
    Example logic using GitHub API:
    - List open issues
    - If label is completed or wontfix, close issue
    This script is intended to be used in GitHub Actions with GITHUB_TOKEN.
    """
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
    # In workflow context, use github API via gh cli or PyGithub:
    # for issue in repo.get_issues(state="open"):
    #     labels = [lbl.name for lbl in issue.labels]
    #     if should_close_issue(labels):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    close_issues_example()
