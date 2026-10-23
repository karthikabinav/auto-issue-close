"use strict";

const test = require("node:test");
const assert = require("node:assert/strict");
const closeIssues = require("./close-completed-wontfix-20261023.js");
const { shouldClose, parseIssueNumbers } = closeIssues;

const issue = (label, extra = {}) => ({
  state: "open", labels: [{ name: label }], ...extra
});

function harness(fixtures, payload = {}) {
  const updates = [];
  return {
    updates,
    args: {
      github: { rest: { issues: {
        get: async ({ issue_number }) => ({ data: fixtures[issue_number] }),
        update: async params => { updates.push(params); }
      } } },
      context: { repo: { owner: "test-owner", repo: "test-repo" }, payload },
      core: { info() {} }
    }
  };
}

test("only completed or wontfix labels qualify", () => {
  assert.equal(shouldClose(issue("completed")), true);
  assert.equal(shouldClose(issue("wontfix")), true);
  assert.equal(shouldClose(issue("bug")), false);
  assert.equal(shouldClose(issue("bug", { labels: [] })), false);
  assert.equal(shouldClose(issue("completed", { state: "closed" })), false);
  assert.equal(shouldClose(issue("completed", { pull_request: {} })), false);
});

test("the three samples close completed and wontfix but leave bug untouched", async () => {
  const h = harness({ 1: issue("completed"), 2: issue("wontfix"), 3: issue("bug") });
  await closeIssues({ ...h.args, issueNumbers: [1, 2, 3] });
  assert.deepEqual(h.updates, [
    { owner: "test-owner", repo: "test-repo", issue_number: 1, state: "closed", state_reason: "completed" },
    { owner: "test-owner", repo: "test-repo", issue_number: 2, state: "closed", state_reason: "not_planned" }
  ]);
});

test("current labels override a stale event; closed issues and pull requests are ignored", async () => {
  const h = harness({
    1: issue("bug"),
    2: issue("completed", { state: "closed" }),
    3: issue("wontfix", { pull_request: {} })
  }, { issue: { number: 1, labels: [{ name: "completed" }] } });
  await closeIssues(h.args);
  await closeIssues({ ...h.args, issueNumbers: [2, 3] });
  assert.deepEqual(h.updates, []);
});

test("manual inputs are validated and duplicate issue numbers removed", async () => {
  assert.deepEqual(parseIssueNumbers("1, 2,3,1"), [1, 2, 3]);
  for (const input of ["", "0", "-1", "1;anything", "1,", "9007199254740992"]) {
    assert.throws(() => parseIssueNumbers(input));
  }
  const h = harness({});
  await assert.rejects(closeIssues({ ...h.args, issueNumbers: [0] }));
  await assert.rejects(closeIssues({ ...h.args, issueNumbers: [] }));
  assert.deepEqual(h.updates, []);
});
