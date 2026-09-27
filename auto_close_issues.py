"""Automatically close issues labeled as completed or wontfix."""
import os
import requests

CLOSING_LABELS = {"completed", "wontfix"}

def main():
    repo = os.environ["GITHUB_REPOSITORY"]
    token = os.environ["GITHUB_TOKEN"]
    headers = {"Authorization": "Bearer " + token, "Accept": "application/vnd.github+json"}
    url = "https://api.github.com/repos/" + repo + "/issues"
    response = requests.get(url, params={"state": "open"}, headers=headers, timeout=30)
    response.raise_for_status()
    for issue in response.json():
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels.intersection(CLOSING_LABELS):
            number = issue["number"]
            close = requests.patch(url + "/" + str(number), json={"state": "closed"}, headers=headers, timeout=30)
            close.raise_for_status()
            print("Closed #{}: {}".format(number, issue["title"]))

if __name__ == "__main__":
    main()
