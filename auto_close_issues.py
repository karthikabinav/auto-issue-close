"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix in auto-issue-close repo.
For learning GitHub automation.
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & TARGET_LABELS)

def close_issues_for_repo(owner, repo):
    """
    Pseudo-code for automation:
    - list open issues
    - for each issue, if label in TARGET_LABELS, update issue state to closed
    - add comment explaining auto-close
    """
    print(f"Checking open issues in {owner}/{repo} for labels {TARGET_LABELS}")
    # Implementation would use GitHub API:
    # issues = list_issues(owner, repo, state="open")
    # for issue in issues:
    #     if should_close_issue(issue["labels"]):
    #         add_issue_comment(owner, repo, issue["number"], "Auto-closing: label is completed/wontfix")
    #         update_issue(owner, repo, issue["number"], state="closed")

if __name__ == "__main__":
    close_issues_for_repo("karthikabinav", "auto-issue-close")
