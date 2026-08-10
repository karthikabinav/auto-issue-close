"""
Automated Issue Closing Script
Closes GitHub issues labeled as "completed" or "wontfix".
"""
import os
from github import Github

# Or use PyGithub or REST API
# This script demonstrates the core logic for automation

LABELS_TO_CLOSE = ["completed", "wontfix"]

def should_close_issue(labels):
    """Check if issue has a label that should trigger auto-close."""
    label_names = [l.name if hasattr(l, "name") else l for l in labels]
    return any(label in LABELS_TO_CLOSE for label in label_names)

def close_issues_in_repo(repo_name, token=None):
    """
    Close open issues in a repository that have completed or wontfix labels.
    Designed to be used in GitHub Actions or as a standalone script.
    """
    token = token or os.getenv("GITHUB_TOKEN")
    if not token:
        print("No GITHUB_TOKEN provided, running in dry-run mode with logic demonstration")
        return
    
    g = Github(token)
    repo = g.get_repo(repo_name)
    open_issues = repo.get_issues(state="open")
    
    for issue in open_issues:
        if issue.pull_request:
            continue
        labels = [label.name for label in issue.labels]
        matched = [lbl for lbl in labels if lbl in LABELS_TO_CLOSE]
        if matched:
            print(f"Closing issue #{issue.number}: {issue.title} - matched labels: {matched}")
            issue.create_comment(f"🤖 Automatically closed: This issue is labeled as {"", "".join(matched)}.")
            # Determine state_reason
            reason = "not_planned" if "wontfix" in matched else "completed"
            issue.edit(state="closed", state_reason=reason)

if __name__ == "__main__":
    # Example usage
    # close_issues_in_repo("karthikabinav/auto-issue-close")
    print(f"Automation script ready. Will close issues with labels: {LABELS_TO_CLOSE}")
    # Demonstration of labeling logic
    test_labels = [["completed"], ["wontfix"], ["bug"], ["enhancement", "completed"]]
    for labels in test_labels:
        print(f"Labels {labels} -> should close: {should_close_issue(labels)}")
