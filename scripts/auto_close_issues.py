"""
Automated Issue Closing script
Closes GitHub issues labeled as completed or wontfix.
"""
import os

# Labels that trigger auto-close
AUTO_CLOSE_LABELS = {"completed", "wontfix"}

def should_close(labels):
    """Return True if issue should be auto-closed based on labels."""
    label_names = {l["name"] if isinstance(l, dict) else l for l in labels}
    return bool(label_names & AUTO_CLOSE_LABELS)

def close_issues_for_repo(owner, repo, token=None):
    """
    Example automation logic using GitHub REST API.
    In GitHub Actions, use GITHUB_TOKEN to list and close issues.
    """
    import urllib.request
    import urllib.parse
    import json
    if not token:
        token = os.getenv("GITHUB_TOKEN", "")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}" if token else "",
    }
    # List open issues
    url = f"https://api.github.com/repos/{owner}/{repo}/issues?state=open&per_page=100"
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as resp:
        issues = json.loads(resp.read().decode())
    for issue in issues:
        # Skip pull requests
        if "pull_request" in issue:
            continue
        labels = [l["name"] for l in issue.get("labels", [])]
        if should_close(labels):
            number = issue["number"]
            print(f"Closing issue #{number}: {issue[title]} with labels {labels}")
            # Close issue via PATCH
            data = json.dumps({"state": "closed"}).encode()
            close_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}"
            close_req = urllib.request.Request(close_url, data=data, headers={**headers, "Content-Type": "application/json"}, method="PATCH")
            with urllib.request.urlopen(close_req) as close_resp:
                print(f"Closed #{number}: {close_resp.status}")
            # Add comment
            comment_data = json.dumps({"body": "Automatically closed because it was labeled as completed or wontfix."}).encode()
            comment_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{number}/comments"
            comment_req = urllib.request.Request(comment_url, data=comment_data, headers={**headers, "Content-Type": "application/json"}, method="POST")
            with urllib.request.urlopen(comment_req) as comment_resp:
                print(f"Commented on #{number}: {comment_resp.status}")

if __name__ == "__main__":
    # Example usage: python auto_close_issues.py <owner> <repo>
    import sys
    if len(sys.argv) >= 3:
        close_issues_for_repo(sys.argv[1], sys.argv[2])
    else:
        print("Usage: python auto_close_issues.py <owner> <repo>")
        print("Checks open issues and closes those labeled completed or wontfix.")
