"""Close open issues labeled completed or wontfix."""
import os
from github import Github

LABELS_TO_CLOSE = {"completed", "wontfix"}

def main():
    repo = Github(os.environ["GITHUB_TOKEN"]).get_repo(os.environ["GITHUB_REPOSITORY"])
    for issue in repo.get_issues(state="open"):
        if LABELS_TO_CLOSE.intersection(label.name for label in issue.labels):
            issue.edit(state="closed")

if __name__ == "__main__":
    main()
