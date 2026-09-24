"""Script to automatically close issues labeled as completed or wontfix."""
# This is a learning example for GitHub automation
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in TARGET_LABELS for label in labels)

def example():
    issues = [
        {"title": "Implement new feature", "labels": ["completed"]},
        {"title": "Remove legacy code", "labels": ["wontfix"]},
        {"title": "Fix login error", "labels": ["bug"]},
    ]
    for issue in issues:
        if should_close(issue["labels"]):
            print(f"Would close: {issue["title"]} with labels {issue["labels"]}")
        else:
            print(f"Keep open: {issue["title"]}")

if __name__ == "__main__":
    example()
