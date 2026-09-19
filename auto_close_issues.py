"""Close issues labeled completed or wontfix via GitHub API."""
import os, requests
LABELS_TO_CLOSE = {"completed", "wontfix"}
# Uses GITHUB_TOKEN env var, lists open issues and patches those with target labels to closed.
