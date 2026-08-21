# Automation Learning Guide - Safe Issue Closing

This guide demonstrates GitHub automation for closing labeled issues safely.

## Workflow Overview

Existing workflow `.github/workflows/auto-close-issues.yml`:
```yaml
name: Auto Close Labeled Issues
on:
  issues:
    types: [opened, labeled]
jobs:
  auto-close:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Close completed or wontfix issues
        uses: actions/github-script@v7
        with:
          script: |
            const issue = context.payload.issue;
            const labels = issue.labels.map(l => l.name);
            if (labels.includes("completed") || labels.includes("wontfix")) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issue.number,
                state: "closed"
              });
            }
```

## Safety Recommendations

- Test in isolated repository (like this `auto-issue-close` repo) before production use
- Use `dry_run: true` to log actions without closing
- Require manual review for 'wontfix' closures
- Limit to specific labels only (completed, wontfix) - 'bug' should remain open
- Monitor workflow runs and audit closed issues regularly

## Python Example (Safe Dry-Run)

See `scripts/safe_auto_close_example.py` for a Python script that:
- Lists issues with labels completed/wontfix
- Logs what WOULD be closed (dry-run by default)
- Requires --confirm flag to actually close
- Never closes issues labeled 'bug'

## Test Results (2026-08-21)

- Issue #1300 'Implement new feature' (completed) -> auto-closed ✓
- Issue #1301 'Remove legacy code' (wontfix) -> auto-closed ✓
- Issue #1302 'Fix login error' (bug) -> remains open ✓

This demonstrates automation works as expected while preserving 'bug' issues.
