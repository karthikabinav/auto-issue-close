# Safe example: How to close issues labeled completed/wontfix
# This is for learning only - DRY RUN mode, does not auto-close.
# Always review issues manually before closing.

# Example logic (pseudocode):
# 1. List open issues
# 2. Check if label is "completed" or "wontfix"
# 3. Require manual confirmation before closing
# 4. Use: update_issue(owner, repo, issue_number, state="closed") only after review

print("Example script - dry run, no issues will be closed automatically.")
print("To test manually, review open issues with labels completed/wontfix")
print("and close them via the GitHub UI after verification.")
