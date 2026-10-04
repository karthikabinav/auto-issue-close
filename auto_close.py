# Automated Issue Closing
# Closes open issues labeled as completed or wontfix

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return bool(set(issue_labels) & CLOSE_LABELS)

# Automation logic:
# for issue in list_open_issues(owner, repo):
#     labels = [label["name"] for label in issue.get("labels", [])]
#     if should_close(labels):
#         update_issue(owner, repo, issue["number"], state="closed")

if __name__ == "__main__":
    print("Auto-close issues labeled completed or wontfix")
