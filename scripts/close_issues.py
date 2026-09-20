#!/usr/bin/env python3
import subprocess, json
LABELS_TO_CLOSE={"completed","wontfix"}
issues=json.loads(subprocess.check_output(["gh","issue","list","--state","open","--json","number,labels","--limit","100"]))
for issue in issues:
 labels={l["name"] for l in issue.get("labels",[])}
 if labels & LABELS_TO_CLOSE:
  subprocess.check_call(["gh","issue","close",str(issue["number"])])
