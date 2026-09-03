"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue has target label."""
    label_names = {l.lower() if isinstance(l, str) else l.get("name", "").lower() for l in labels}
    return bool(label_names & TARGET_LABELS)

def main():
    # Example logic for GitHub Actions or manual use
    # In production, use PyGithub or GitHub API to list and close issues
    print("Checking for issues labeled as completed or wontfix to close...")
    # Pseudo:
    # for issue in repo.get_issues(state="open"):
    #     if should_close([label.name for label in issue.labels]):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}")

if __name__ == "__main__":
    main()
