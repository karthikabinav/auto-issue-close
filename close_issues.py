"""
Automation script to close issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label.lower() in AUTO_CLOSE_LABELS for label in labels)

def main():
    # Example logic for GitHub Actions or local use
    # In real workflow, use PyGithub or gh api to list and close issues
    print("Checking issues for auto-close labels:", AUTO_CLOSE_LABELS)
    # Placeholder: integrate with GitHub API
    # e.g., for issue in repo.get_issues(state=open):
    #           if should_close([l.name for l in issue.labels]):
    #               issue.edit(state=closed)
    #               print(f"Closed issue #{issue.number}")

if __name__ == "__main__":
    main()
