# Example automation script for learning GitHub automation
# This script demonstrates how to close issues labeled as completed or wontfix.
# NOTE: Review issues manually before running in production. Do not auto-run without approval.
#
# Usage:
#   1. Review open issues with labels completed / wontfix
#   2. Run manually to close after verification
#
# Example logic (pseudo-code):
#   - list open issues
#   - if label in [completed, wontfix]:
#       - add comment explaining closure
#       - close issue
#
AUTO_CLOSE_LABELS = ["completed", "wontfix"]

def should_close(labels):
    return any(lbl in AUTO_CLOSE_LABELS for lbl in labels)

if __name__ == "__main__":
    print("Example script - manual review required before closing issues.")
    print(f"Would auto-close labels: {AUTO_CLOSE_LABELS}")
