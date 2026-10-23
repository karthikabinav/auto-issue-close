"use strict";

const CLOSE_LABELS = new Set(["completed", "wontfix"]);

// Only open issues with a matching label qualify; pull requests are excluded.
function shouldClose(issue) {
  return Boolean(issue && !issue.pull_request && issue.state === "open" &&
    Array.isArray(issue.labels) &&
    issue.labels.some(label => CLOSE_LABELS.has(label.name)));
}

function parseIssueNumbers(value) {
  const parts = value.split(",").map(part => part.trim());
  if (parts.some(part => !/^[1-9]\d*$/.test(part) ||
      !Number.isSafeInteger(Number(part)))) {
    throw new Error("Provide comma-separated positive integer issue numbers.");
  }
  return [...new Set(parts.map(Number))];
}

async function closeIssues({ github, context, core, issueNumbers }) {
  const numbers = issueNumbers === undefined
    ? [context.payload.issue?.number]
    : issueNumbers;
  if (!Array.isArray(numbers) || numbers.length === 0 ||
      numbers.some(number => !Number.isSafeInteger(number) || number <= 0)) {
    throw new Error("At least one valid issue number is required.");
  }
  const { owner, repo } = context.repo;
  for (const issue_number of new Set(numbers)) {
    // Re-read current labels and state instead of trusting a stale event payload.
    const { data: issue } = await github.rest.issues.get({ owner, repo, issue_number });
    if (!shouldClose(issue)) {
      core.info(`Leaving issue #${issue_number} unchanged.`);
      continue;
    }
    const state_reason = issue.labels.some(label => label.name === "completed")
      ? "completed" : "not_planned";
    await github.rest.issues.update({
      owner, repo, issue_number, state: "closed", state_reason
    });
    core.info(`Closed issue #${issue_number} (${state_reason}).`);
  }
}

module.exports = closeIssues;
module.exports.shouldClose = shouldClose;
module.exports.parseIssueNumbers = parseIssueNumbers;
