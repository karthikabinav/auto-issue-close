# Automated Issue Closing script
# Closes issues labeled as completed or wontfix

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in TARGET_LABELS for label in labels)

# Example usage with GitHub API:
# - List open issues
# - If issue has label completed or wontfix, update state to closed
print("Auto-close script ready: will close issues with labels: completed, wontfix")
