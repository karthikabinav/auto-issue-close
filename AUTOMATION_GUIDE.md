# Safe Automation Guide - Educational Example

## ⚠️ Safety Warning
Automatically closing issues based on labels can be destructive. It may close important issues prematurely, lose context, and bypass human review. Always require manual approval before enabling destructive automation in production repositories.

## Existing Repository State
This repository already contains workflows that auto-close issues labeled `completed` or `wontfix`:
- `.github/workflows/auto-close-issues.yml`
- `.github/workflows/auto-close-labeled.yml`
- etc.

These workflows are active and will automatically close newly labeled issues. Review them carefully before testing.

## Educational Example (Disabled by Default)
Below is an example of how such automation *could* be implemented, presented for learning only. This example is NOT active and should not be deployed without review.

```yaml
# Example - DO NOT ENABLE WITHOUT REVIEW
# name: Example Auto Close (Disabled)
# on:
#   issues:
#     types: [labeled]
# jobs:
#   check-label:
#     runs-on: ubuntu-latest
#     steps:
#       - name: Log label event (safe - no destructive action)
#         run: echo "Issue ${{ github.event.issue.number }} labeled with ${{ github.event.label.name }}"
#       # DANGER: The following step would automatically close issues - requires human approval
#       # - uses: actions/github-script@v7
#       #   with:
#       #     script: |
#       #       // Only close after manual review!
#       #       console.log("Would close issue", context.payload.issue.number)
```

## Recommended Safe Testing Approach
1. Create test issues with `completed`, `wontfix`, and `bug` labels (done: issues #615, #616, #617)
2. Observe existing workflow behavior without adding new destructive automation
3. For `bug` label, issue should remain open (expected)
4. For `completed`/`wontfix`, existing workflows will auto-close - this is destructive and should be monitored
5. Always add a comment explaining closure reason and require human review before closing

## Best Practices
- Require manual approval or a second label like `verified` before auto-closing
- Add a delay (e.g., 7 days) before closing
- Notify assignees and allow opt-out
- Log all automated actions for audit
- Test in a separate repository first

## Test Issues Created
- #615 - Implement new feature (completed) - will be auto-closed by existing workflow
- #616 - Remove legacy code (wontfix) - will be auto-closed by existing workflow  
- #617 - Fix login error (bug) - should remain open

For learning purposes, no new destructive workflow was added. Please review existing workflows with your instructor before enabling further automation.
