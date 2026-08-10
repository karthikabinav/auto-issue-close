# Automated Issue Closing Script

This script automatically closes GitHub issues labeled as `completed` or `wontfix`.

## GitHub Actions Workflow

Place this in `.github/workflows/auto-close.yml`:

```yaml
name: Auto Close Labeled Issues
on:
  issues:
    types: [opened, labeled, edited, reopened]
jobs:
  auto-close:
    runs-on: ubuntu-latest
    permissions:
      issues: write
    steps:
      - name: Check labels and close issue
        uses: actions/github-script@v7
        with:
          script: |
            const labels = context.payload.issue.labels.map(l => l.name);
            if (labels.includes("completed") || labels.includes("wontfix")) {
              await github.rest.issues.update({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                state: "closed"
              });
              await github.rest.issues.createComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                issue_number: context.issue.number,
                body: "✅ Automatically closed by automation: issue labeled as `completed` or `wontfix`."
              });
            }
```

## Testing

Created three sample issues:
- "Implement new feature" with label `completed` → should auto-close
- "Remove legacy code" with label `wontfix` → should auto-close  
- "Fix login error" with label `bug` → should stay open
