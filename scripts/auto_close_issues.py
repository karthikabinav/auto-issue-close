"""
Automated Issue Closing Script
Automatically closes issues labeled as completed or wontfix.
"""

AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_for_repo(owner, repo):
    """
    Example automation logic using GitHub API:
    - List open issues
    - If issue has label completed or wontfix, close it
    """
    # Pseudo-code for GitHub workflow:
    # issues = github.rest.issues.listForRepo({owner, repo, state: "open"})
    # for issue in issues:
    #     if should_close_issue(issue.labels):
    #         github.rest.issues.update({owner, repo, issue_number: issue.number, state: "closed"})
    print(f"Checking issues in {owner}/{repo} for labels {AUTO_CLOSE_LABELS}")

if __name__ == "__main__":
    close_issues_for_repo("karthikabinav", "auto-issue-close")
