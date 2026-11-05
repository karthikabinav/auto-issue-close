# Automated Issue Closing Script
# Closes issues labeled as completed or wontfix
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in TARGET_LABELS for l in labels)

print("Auto-close ready")
