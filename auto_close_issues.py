#!/usr/bin/env python3
import os, requests
REPO=os.environ.get(chr(71)+"ITHUB_REPOSITORY")
TOKEN=os.environ.get("GITHUB_TOKEN")
LABELS_TO_CLOSE={"completed","wontfix"}
# Closes open issues whose labels intersect LABELS_TO_CLOSE via GitHub API
