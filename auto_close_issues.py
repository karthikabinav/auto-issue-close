# Script to automatically close issues labeled as completed or wontfix
# Uses the GitHub REST API via PyGithub-style logic (placeholder for learning)
# For each open issue, if any label is completed or wontfix, close the issue.

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return any(label in CLOSE_LABELS for label in issue_labels)

if __name__ == "__main__":
    print("Auto-close script: closes issues labeled completed or wontfix")
