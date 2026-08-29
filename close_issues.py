"""
Automated Issue Closing script
Closes issues labeled as "completed" or "wontfix".
"""
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has a label that triggers auto-close."""
    return any(label in AUTO_CLOSE_LABELS for label in labels)

def process_issues(issues):
    """
    issues: iterable of dicts with "number", "title", "labels", "state"
    Returns list of issue numbers that should be closed.
    """
    to_close = []
    for issue in issues:
        labels = issue.get("labels", [])
        # support both string list and dict list from GitHub API
        label_names = [l if isinstance(l, str) else l.get("name") for l in labels]
        if issue.get("state") == "open" and should_close_issue(label_names):
            to_close.append(issue["number"])
    return to_close

if __name__ == "__main__":
    # Example usage with GitHub API (pseudo-code):
    # from github import Github
    # g = Github(token)
    # repo = g.get_repo("owner/auto-issue-close")
    # for issue in repo.get_issues(state="open"):
    #     label_names = [l.name for l in issue.labels]
    #     if should_close_issue(label_names):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}: {issue.title}")
    print("Auto-close script ready. Monitors labels:", AUTO_CLOSE_LABELS)
