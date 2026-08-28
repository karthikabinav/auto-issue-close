"""
Automation script to automatically close issues labeled as completed or wontfix.
This script is for learning GitHub automation.
"""
# In a real workflow, this would use the GitHub API to list open issues
# and close those with labels completed or wontfix.
# Example logic:
#   for issue in open_issues:
#       labels = [l[name] for l in issue[labels]]
#       if completed in labels or wontfix in labels:
#           close_issue(issue[number])
print("Automation script: would close issues labeled completed or wontfix")
