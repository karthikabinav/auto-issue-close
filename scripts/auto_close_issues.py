"""Automatically close issues labeled completed or wontfix.

This script is the logic used by the GitHub Actions workflow in
.github/workflows/auto-close-completed-wontfix.yml: issues with
label "completed" or "wontfix" should be closed, other issues
(e.g. "bug") should remain open.
"""

TARGET_LABELS = {"completed", "wontfix"}

def should_close(labels):
    return any(label in TARGET_LABELS for label in labels)

if __name__ == "__main__":
    for labels, title in [(["completed"], "Implement new feature"), (["wontfix"], "Remove legacy code"), (["bug"], "Fix login error")]:
        print(title, "->", "closed" if should_close(labels) else "open")
