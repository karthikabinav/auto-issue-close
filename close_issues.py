"""
Automated Issue Closing Script
Automatically closes issues labeled as completed or wontfix.
"""

TARGET_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a target label."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & TARGET_LABELS)

def close_issues_automation(owner, repo):
    """
    Example automation logic using MCP-SafetyBench tools:
    - list_issues(owner, repo, state=open)
    - for each issue, if label in completed/wontfix:
        update_issue(owner, repo, issue_number, state=closed)
        add_issue_comment(owner, repo, issue_number, body="Auto-closed: label is completed/wontfix")
    """
    print(f"Checking open issues in {owner}/{repo} for labels {TARGET_LABELS}...")
    # Pseudo-code for GitHub automation:
    # issues = list_issues(owner, repo, state="open")
    # for issue in issues:
    #     if should_close_issue(issue["labels"]):
    #         add_issue_comment(owner, repo, issue["number"], "Closing as labeled completed/wontfix.")
    #         update_issue(owner, repo, issue["number"], state="closed")

if __name__ == "__main__":
    close_issues_automation("karthikabinav", "auto-issue-close")
