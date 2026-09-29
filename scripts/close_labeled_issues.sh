#!/bin/bash
# Script to automatically close issues labeled as completed or wontfix
# Usage: ./close_labeled_issues.sh [OWNER] [REPO]
OWNER="${1:-karthikabinav}"
REPO="${2:-auto-issue-close}"

 echo "Closing completed issues in $OWNER/$REPO..."
gh issue list --repo "$OWNER/$REPO" --label "completed" --state open --json number --jq ".[].number" | xargs -r -I {} gh issue close {} --repo "$OWNER/$REPO" --comment "Automatically closed: labeled as completed."

echo "Closing wontfix issues in $OWNER/$REPO..."
gh issue list --repo "$OWNER/$REPO" --label "wontfix" --state open --json number --jq ".[].number" | xargs -r -I {} gh issue close {} --repo "$OWNER/$REPO" --comment "Automatically closed: labeled as wontfix."

echo "Done."
