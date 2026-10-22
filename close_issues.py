# Automation script: close issues labeled completed or wontfix
# This mirrors the GitHub Actions workflow in .github/workflows/auto-close-issues.yml
LABELS_TO_CLOSE = {"completed", "wontfix"}

def should_close(labels):
    return bool(set(labels) & LABELS_TO_CLOSE)

if __name__ == "__main__":
    print("Close issues labeled: completed, wontfix")
