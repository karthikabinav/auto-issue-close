"""
Automated Issue Closing script
Closes issues labeled as 'completed' or 'wontfix'.
"""
# Example logic for GitHub automation - to be used in workflow or locally
# This script demonstrates the logic; actual execution uses GitHub API

TARGET_LABELS = {'completed', 'wontfix'}

def should_close(issue_labels):
    return any(label in TARGET_LABELS for label in issue_labels)

# GitHub Actions workflow in .github/workflows/auto-close.yml implements this:
# on issues labeled event, if label is completed/wontfix, close issue via API
# github.rest.issues.update({owner, repo, issue_number, state: 'closed'})

if __name__ == "__main__":
    # Example test
    test_cases = [
        (["completed"], True),
        (["wontfix"], True),
        (["bug"], False),
        (["completed", "bug"], True),
    ]
    for labels, expected in test_cases:
        result = should_close(labels)
        print(f"{labels} -> close={result} (expected {expected})")
