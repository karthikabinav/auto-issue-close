#!/usr/bin/env python3
"""Automatically close issues labeled as completed or wontfix.

The automation-equivalent script for this repository. It queries the GitHub
REST API, finds every open issue that carries the "completed" or "wontfix"
label, and closes it.

Environment variables:
    GH_TOKEN: personal access token or fine-grained token with
              "issues: write" permission.
    GH_REPO:  repository in owner/name form (default: karthikabinav/auto-issue-close).
"""

import json
import os
import sys
import urllib.request

TARGET_LABELS = {"completed", "wontfix"}
CLOSE_COMMENT = (
    "Automatically closed by the issue-cleanup automation: "
    "this issue is labeled as completed or wontfix."
)


def github_request(method, url, extra_headers=None, payload=None):
    headers = {
        "Authorization": "Bearer " + os.environ["GH_TOKEN"],
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if extra_headers:
        headers.update(extra_headers)
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def list_open_issues(repo):
    url = "https://api.github.com/repos/{}/issues?state=open&per_page=100".format(repo)
    return github_request("GET", url)


def close_issue(repo, issue_number):
    close_url = "https://api.github.com/repos/{}/issues/{}".format(repo, issue_number)
    github_request("PATCH", close_url, payload={"state": "closed"})
    comment_url = close_url + "/comments"
    github_request("POST", comment_url, payload={"body": CLOSE_COMMENT})


def main():
    if not os.environ.get("GH_TOKEN"):
        sys.stderr.write("Error: GH_TOKEN environment variable is not set.\n")
        sys.exit(1)
    repo = os.environ.get("GH_REPO", "karthikabinav/auto-issue-close")
    closed = []
    for issue in list_open_issues(repo):
        if "pull_request" in issue:
            continue
        labels = {label["name"] for label in issue.get("labels", [])}
        if labels & TARGET_LABELS:
            close_issue(repo, issue["number"])
            closed.append(issue["number"])
            print("Closed issue #{}: {}".format(issue["number"], issue["title"]))
    print("Done. Closed {} issue(s).".format(len(closed)))


if __name__ == "__main__":
    main()
