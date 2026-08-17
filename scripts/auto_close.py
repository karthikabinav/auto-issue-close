import os
from github import Github

# Initialize GitHub client
# Requires GITHUB_TOKEN environment variable
token = os.getenv("GITHUB_TOKEN")
if not token:
    raise ValueError("GITHUB_TOKEN environment variable not set")

g = Github(token)

# Get repository (update owner/repo as needed)
repo_name = os.getenv("GITHUB_REPOSITORY", "karthikabinav/auto-issue-close")
repo = g.get_repo(repo_name)

# Labels that should trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(issue):
    """Check if issue has labels that require auto-closing."""
    labels = {label.name for label in issue.labels}
    return bool(labels & AUTO_CLOSE_LABELS)

def close_issues():
    """Close open issues with completed or wontfix labels."""
    open_issues = repo.get_issues(state="open")
    for issue in open_issues:
        if should_close_issue(issue):
            print(f"Closing issue #{issue.number}: {issue.title} - labels: {[l.name for l in issue.labels]}")
            issue.create_comment("This issue has been automatically closed because it was labeled as completed or wontfix.")
            issue.edit(state="closed")

if __name__ == "__main__":
    close_issues()
    print("Auto-close script completed.")
