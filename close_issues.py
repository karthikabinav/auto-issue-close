"""Automation script to close issues labeled as completed or wontfix."""
# This script demonstrates the logic used in .github/workflows/auto-close.yml
# It closes any open issue that has label 'completed' or 'wontfix'.

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return any(label in TARGET_LABELS for label in issue_labels)

# Example usage with GitHub API (pseudo-code):
# for issue in list_open_issues():
#     labels = [l["name"] for l in issue["labels"]]
#     if should_close(labels):
#         close_issue(issue["number"])

if __name__ == "__main__":
    print("Automation ready: will close issues labeled as completed or wontfix")
