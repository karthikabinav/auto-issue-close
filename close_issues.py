# Automation script to close issues labeled as completed or wontfix
"""
This script automatically closes issues labeled as completed or wontfix.
It can be used as a GitHub Action or run manually.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Check if issue should be closed based on labels."""
    label_names = {label.lower() if isinstance(label, str) else label.get("name", "").lower() for label in labels}
    return bool(label_names.intersection(AUTO_CLOSE_LABELS))

def close_issues_example():
    """
    Example logic for GitHub Actions using github-script or PyGithub.
    In a real workflow, you would use:
    - github.rest.issues.update() to close the issue
    - Check github.event.issue.labels for triggers
    """
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
    # Placeholder for actual GitHub API integration
    # Example with PyGithub:
    # from github import Github
    # g = Github(os.environ["GITHUB_TOKEN"])
    # repo = g.get_repo(os.environ["GITHUB_REPOSITORY"])
    # for issue in repo.get_issues(state="open"):
    #     labels = [l.name for l in issue.get_labels()]
    #     if should_close_issue(labels):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    close_issues_example()
