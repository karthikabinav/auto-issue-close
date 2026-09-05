"""
Automated Issue Closing Script
Closes issues labeled as completed or wontfix.
"""
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    return any(label.lower() in AUTO_CLOSE_LABELS for label in labels)

def main():
    print("Auto-close script: closes issues labeled as completed or wontfix")
    sample_issues = [
        {"number": 1, "title": "Implement new feature", "labels": ["completed"]},
        {"number": 2, "title": "Remove legacy code", "labels": ["wontfix"]},
        {"number": 3, "title": "Fix login error", "labels": ["bug"]},
    ]
    for issue in sample_issues:
        num = issue["number"]
        title = issue["title"]
        labels = issue["labels"]
        if should_close(labels):
            print(f"Would close #{num}: {title} labels={labels}")
        else:
            print(f"Would keep open #{num}: {title} labels={labels}")

if __name__ == "__main__":
    main()
