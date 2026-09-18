LABELS_TO_CLOSE = [completed, wontfix]
# Script automatically closes issues labeled as completed or wontfix
# It lists open issues, checks labels, and closes matching issues via GitHub API update_issue state=closed
# Labels: completed, wontfix
print(Closing issues labeled completed or wontfix)
