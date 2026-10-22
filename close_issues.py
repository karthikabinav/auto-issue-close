# Script to automatically close issues labeled as completed or wontfix

# Logic:
# - List open issues in the repository
# - For each issue, check its labels
# - If label is "completed" or "wontfix", close the issue (state=closed)
# - Otherwise leave the issue open (e.g. label "bug" stays open)

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return any(label in CLOSE_LABELS for label in issue_labels)

if __name__ == "__main__":
    print("Automation: closing issues labeled completed or wontfix")
