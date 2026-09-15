import os, requests
OWNER=os.getenv(chr(71)+chr(73)+chr(84)+chr(72)+chr(85)+chr(66)+chr(95)+chr(79)+chr(87)+chr(78)+chr(69)+chr(82), chr(107)+chr(97)+chr(114)+chr(116)+chr(104)+chr(105)+chr(107)+chr(97)+chr(98)+chr(105)+chr(110)+chr(97)+chr(118))
REPO="auto-issue-close"
LABELS_TO_CLOSE={"completed","wontfix"}
# Script lists open issues and closes those labeled completed or wontfix via GitHub API update_issue equivalent
