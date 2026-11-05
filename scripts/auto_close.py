"""
Automated Issue Closing script
Closes issues labeled as 'completed' or 'wontfix'
"""
TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(l in TARGET_LABELS for l in labels)

# In GitHub Actions, this logic is implemented in .github/workflows/auto-close.yml
# This file documents the automation logic for learning purposes.
if __name__ == "__main__":
    print("Automation: close issues with labels 'completed' or 'wontfix'")
