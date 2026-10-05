# Automated Issue Closing
# Closes open issues labeled as completed or wontfix

CLOSE_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    return bool(set(issue_labels) & CLOSE_LABELS)

if __name__ == "__main__":
    print("Auto-close issues labeled completed or wontfix")
