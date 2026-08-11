# Automated Issue Closing Guide

This repository demonstrates GitHub automation for automatically closing issues.

## Workflow Trigger

The workflow runs when an issue is labeled with:
- `completed`
- `wontfix`

## How It Works

File: `.github/workflows/auto-close-issues.yml`

```yaml
name: Auto Close Labeled Issues
on:
  issues:
    types: [labeled]
jobs:
  auto-close:
    runs-on: ubuntu-latest
    if: contains('completed wontfix', github.event.label.name)
    steps:
      - name: Close issue
        uses: actions/github-script@v7
        with:
          script: |
            const label = context.payload.label.name;
            const issueNumber = context.issue.number;
            if (label === 'completed' || label === 'wontfix') {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: issueNumber,
                state: 'closed'
              });
            }
```

## Test Results

- Issue "Implement new feature" with label `completed` → **Closed automatically**
- Issue "Remove legacy code" with label `wontfix` → **Closed automatically**
- Issue "Fix login error" with label `bug` → **Remains open**

This confirms the automation works correctly!
