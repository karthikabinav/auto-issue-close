"""
Automation script to close GitHub issues labeled as 'completed' or 'wontfix'.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label.lower() in AUTO_CLOSE_LABELS for label in labels)

def main():
    # Example logic - in real use, integrate with PyGithub or GitHub API
    # For GitHub Actions, the workflow .github/workflows/auto-close-issues.yml handles it
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
    # Placeholder for API integration
    # from github import Github
    # g = Github(os.getenv("GITHUB_TOKEN"))
    # repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
    # for issue in repo.get_issues(state="open"):
    #     labels = [l.name for l in issue.labels]
    #     if should_close(labels):
    #         issue.edit(state="closed")
    #         print(f"Closed issue #{issue.number}: {issue.title}")

if __name__ == "__main__":
    main()
