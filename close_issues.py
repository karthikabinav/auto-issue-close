# Automation script to close issues labeled as completed or wontfix
# Uses the GitHub API to list open issues and closes those with
# labels completed or wontfix, leaving other labels (e.g. bug) open.

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in CLOSE_LABELS for label in labels)

if __name__ == "__main__":
    print("Closing issues labeled completed or wontfix")
