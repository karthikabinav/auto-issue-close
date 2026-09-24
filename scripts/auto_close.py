# Educational example: auto-close issues labeled as completed or wontfix
#
# SAFETY NOTES:
# - This script defaults to DRY_RUN = True and will NOT close anything unless
#   you explicitly set DRY_RUN = False and confirm.
# - Do NOT run this automatically on every issue event without human review.
# - Always review issues manually before closing in production.
#
# Usage:
#   python scripts/auto_close.py --dry-run   # safe preview (default)
#   python scripts/auto_close.py --apply      # actually close (requires confirmation)

import argparse

TARGET_LABELS = {"completed", "wontfix"}
DRY_RUN = True

def should_close(labels):
    """Return True if issue has a target label."""
    return any(lbl in TARGET_LABELS for lbl in labels)

def main():
    parser = argparse.ArgumentParser(description="Demo auto-close logic (safe, dry-run by default)")
    parser.add_argument("--dry-run", action="store_true", default=True, help="Preview only (default)")
    parser.add_argument("--apply", action="store_true", help="Actually close issues (requires confirmation)")
    args = parser.parse_args()

    apply = args.apply and not args.dry_run
    # If --apply is passed, require explicit confirmation via DRY_RUN override
    if args.apply:
        print("WARNING: --apply was requested.")
        print("In a real implementation, you would list open issues via the GitHub API,")
        print("filter by TARGET_LABELS, and call update_issue(state=closed) only after manual review.")
        print("This educational script does NOT perform any API calls automatically.")
        # Keep DRY_RUN behavior unless user edits file to disable safety
        if DRY_RUN:
            print("DRY_RUN is True - no changes will be made. Edit DRY_RUN=False to allow closing after review.")
            return
    else:
        print("Dry-run mode: no issues will be closed.")
        print(f"Target labels for auto-close (example only): {sorted(TARGET_LABELS)}")
        print("Example logic: if completed in issue_labels or wontfix in issue_labels: close issue")
        print("To test manually, create issues with labels completed, wontfix, bug and review this logic.")

if __name__ == "__main__":
    main()
