"""
Automated Issue Closing script
Automatically closes issues labeled as completed or wontfix.
"""
import os

TARGET_LABELS = {"completed", "wontfix"}

def should_close(issue_labels):
    """Return True if issue has a target label."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in issue_labels}
    return bool(label_names & TARGET_LABELS)

def close_issues_for_repo(owner, repo, token):
    """Example automation using GitHub REST API (requires requests)."""
    try:
        import requests
    except ImportError:
        print("requests library required for live run")
        return
    headers = {"Authorization": f"token {token}", "Accept": "application/vnd.github.v3+json"}
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open"
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    for issue in r.json():
        if "pull_request" in issue:
            continue
        labels = [l["name"] for l in issue.get("labels", [])]
        if should_close(labels):
            num = issue["number"]
            print(f"Closing issue #{num}: {issue[title]} with labels {labels}")
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{num}"
            requests.patch(close_url, headers=headers, json={"state": "closed"})

if __name__ == "__main__":
    # Example usage: python close_issues.py <owner> <repo>
    import sys
    if len(sys.argv) == 3:
        tok = os.getenv("GITHUB_TOKEN", "")
        close_issues_for_repo(sys.argv[1], sys.argv[2], tok)
    else:
        print("Demo: should_close([completed]) =", should_close(["completed"]))
        print("Demo: should_close([bug]) =", should_close(["bug"]))
