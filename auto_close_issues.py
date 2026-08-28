"""
Automated Issue Closing script
Closes GitHub issues labeled as 'completed' or 'wontfix'.
"""
import os

AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close_issue(labels):
    label_names = {lbl.lower() if isinstance(lbl, str) else lbl.get("name","").lower() for lbl in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def main():
    print("Auto-close check:", AUTO_CLOSE_LABELS)
    try:
        from github import Github
        g = Github(os.getenv("GITHUB_TOKEN"))
        repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
        for issue in repo.get_issues(state="open"):
            labels = [l.name for l in issue.labels]
            if should_close_issue(labels):
                issue.create_comment("Automatically closing this issue as it was labeled as completed or wontfix.")
                issue.edit(state="closed")
                print(f"Closed #{issue.number}: {issue.title}")
    except Exception as e:
        print(f"Demo mode: {e}")
        for labels in [["completed"], ["wontfix"], ["bug"]]:
            print(f"{labels} -> {should_close_issue(labels)}")

if __name__ == "__main__":
    main()
