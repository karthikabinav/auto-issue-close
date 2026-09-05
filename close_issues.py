"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix.
"""
import os
# This script is intended to be used via GitHub Actions or manually.
# It demonstrates the logic for auto-closing labeled issues.

AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    return any(label.lower() in AUTO_CLOSE_LABELS for label in labels)

def main():
    # Example usage with GitHub API (requires GH_TOKEN):
    # In a real workflow, you would list open issues and close matching ones.
    # For GitHub Actions, see .github/workflows/auto-close-issues.yml
    print("Auto-close script: closes issues labeled as completed or wontfix")
    # Simulated logic
    sample_issues = [
        {"number": 1, "title": "Implement new feature", "labels": ["completed"]},
        {"number": 2, "title": "Remove legacy code", "labels": ["wontfix"]},
        {"number": 3, "title": "Fix login error", "labels": ["bug"]},
    ]
    for issue in sample_issues:
        if should_close(issue["labels"]):
            print(f"Would close #{issue["number"]}: {issue["title"]} labels={issue["labels"]}")
        else:
            print(f"Would keep open #{issue["number"]}: {issue["title"]} labels={issue["labels"]}")

if __name__ == "__main__":
    main()
