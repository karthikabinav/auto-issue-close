#!/usr/bin/env python3
"""Automatically close issues labeled completed or wontfix using GitHub API (gh CLI)."""
import subprocess, json, sys
LABELS_TO_CLOSE = {"completed", "wontfix"}
def main():
    issues = json.loads(subprocess.check_output(["gh", "issue", "list", "--state", "open", "--json", "number,labels", "--limit", "100"]).decode())
    for issue in issues:
        labels = {l["name"] for l in issue.get("labels", [])}
        if labels & LABELS_TO_CLOSE:
            subprocess.check_call(["gh", "issue", "close", str(issue["number"])])
            print(f"Closed #{issue[chr(39)+chr(39)] if False else issue["number"]}")
if __name__ == "__main__":
    main()
