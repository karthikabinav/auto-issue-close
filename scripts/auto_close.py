"""
Automation script to close GitHub issues labeled as completed or wontfix.
This script can be run manually or via GitHub Actions.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    return bool(set(labels) & AUTO_CLOSE_LABELS)

def close_issues_example():
    """Example logic for GitHub Actions using github-script or PyGithub."""
    # In real workflow, use GitHub API:
    # from github import Github
    # g = Github(os.getenv("GITHUB_TOKEN"))
    # repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
    # for issue in repo.get_issues(state="open"):
    #     lbls = [l.name for l in issue.labels]
    #     if should_close(lbls):
    #         issue.create_comment(f"Automatically closing as labeled {lbls}")
    #         issue.edit(state="closed")
    pass

if __name__ == "__main__":
    # Simple test
    assert should_close(["completed"]) == True
    assert should_close(["wontfix"]) == True
    assert should_close(["bug"]) == False
    print("Auto-close logic verified for labels: completed, wontfix")
