import sys

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & CLOSE_LABELS)

def main():
    # Example automation: close issues labeled completed or wontfix
    issues = [
        {"number": 1, "labels": ["completed"]},
        {"number": 2, "labels": ["wontfix"]},
        {"number": 3, "labels": ["bug"]},
    ]
    for issue in issues:
        if should_close(issue["labels"]):
            print(f"Closing issue #{issue["number"]} with labels {issue["labels"]}")
        else:
            print(f"Leaving issue #{issue["number"]} open with labels {issue["labels"]}")

if __name__ == "__main__":
    main()
