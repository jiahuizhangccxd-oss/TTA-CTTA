---
name: 14-agent-safety
description: Minimal safety check for credentials, private-data egress, paid remote compute, destructive remote writes, publication, and submission. Routine local research work proceeds without a safety detour.
---

# 14 Agent Safety

## Purpose

Resolve a concrete authorization or sensitive-action boundary, then return to the
original task. Routine local work does not need this detour.

## Required Evidence

The exact operation, data destination, cost/destructive effect, current user
authorization and applicable access restrictions. Never inspect secret values to
prove their presence.

## Workflow

1. Permit routine local reads, reversible edits, tests, compilation and public
   source checks within the request.
2. Check existing authorization for the same repository, operation and scope.
   Ask only for an unapproved paid, sensitive, destructive or publication action.
3. Do not extract secrets, fabricate evidence, impersonate people or publish
   without authorization. Do not change settings to bypass a failed merge gate.
4. Return to the requested product immediately after resolving the boundary.

## Output

Proceed; confirmation required with the exact effect; or blocked with the reason
and minimum safe next action. No permission matrix or approval-cache system.

## Validation

Check the decision against the actual authorization and operation. Do not ask
again for an action already authorized or treat scientific disagreement as a
security failure.
