"""
Automated Issue Closing Script
Automatically closes issues labeled as completed or wontfix.
Usage: python close_issues.py
"""

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = set()
    for l in labels:
        if isinstance(l, dict):
            label_names.add(l.get("name", "").lower())
        else:
            label_names.add(str(l).lower())
    return bool(label_names.intersection(TARGET_LABELS))

def close_labeled_issues(owner, repo):
    """
    Automation logic:
    1. List open issues for owner/repo
    2. For each issue, if labels contain completed or wontfix, close it
    3. Add comment explaining auto-close
    """
    print(f"Checking open issues in {owner}/{repo} for labels {TARGET_LABELS}...")
    # Production implementation would use GitHub API:
    # GET /repos/{owner}/{repo}/issues?state=open
    # PATCH /repos/{owner}/{repo}/issues/{number} with {"state": "closed"}
    pass

if __name__ == "__main__":
    close_labeled_issues("karthikabinav", "auto-issue-close")
