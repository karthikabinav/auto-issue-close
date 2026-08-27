"""
Automated Issue Closing script
Closes GitHub issues labeled as 'completed' or 'wontfix'.

This script is intended as a learning example for GitHub automation.
It can be run manually or via GitHub Actions.
"""
import os

# Labels that should trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    """Return True if issue has completed or wontfix label."""
    label_names = {lbl.lower() if isinstance(lbl, str) else lbl.get('name','').lower() for lbl in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_example():
    """
    Example logic using PyGithub (pip install PyGithub):
    
    from github import Github
    g = Github(os.getenv('GITHUB_TOKEN'))
    repo = g.get_repo(os.getenv('GITHUB_REPOSITORY'))
    for issue in repo.get_issues(state='open'):
        labels = [l.name for l in issue.labels]
        if should_close_issue(labels):
            issue.create_comment('Automatically closing this issue as it was labeled as completed or wontfix.')
            issue.edit(state='closed')
            print(f"Closed #{issue.number}: {issue.title}")
    """
    print("Auto-close check: labels", AUTO_CLOSE_LABELS)
    # Demo
    test_cases = [["completed"], ["wontfix"], ["bug"], ["enhancement", "completed"]]
    for labels in test_cases:
        print(f"{labels} -> should_close={should_close_issue(labels)}")

if __name__ == "__main__":
    close_issues_example()
