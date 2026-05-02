<!-- BEGIN: Spec Coding -->

## Spec Coding Operating Rules

Use Spec Coding for durable AI development work that should survive chat resets, multiple agents, or long-running implementation.

### Layer Model

```text
Spec -> Plan -> Task
what    how     now
```

- `Spec` is the current source of truth: system behavior, interfaces, invariants, permissions, boundaries, and constraints.
- `Plan` is the implementation strategy: technical path, sequencing, dependencies, orchestration, rollout, rollback, risks, and tradeoffs.
- `Task` is the executable unit: one focused piece of work with acceptance criteria, status, blockers, execution notes, and review results.

### Default Project Memory

- Keep durable AI work under `omni-coding/` unless this project defines a different location.
- Read `omni-coding/specs/current/` as the default current truth.
- Use `omni-coding/specs/drafts/` for unpromoted feature discovery, requirements research, test plans, validation evidence, and candidate Spec Patches.
- Treat `omni-coding/specs/guides/` as explanatory context, not authoritative truth.
- Do not use `omni-coding/specs/log/` or `omni-coding/specs/archive/` as default decision input unless the user explicitly requests historical analysis.
- Use `omni-coding/plans/` for active and historical implementation plans.
- Use `omni-coding/tasks/` for executable tasks, dashboards, inbox capture, execution logs, blockers, and reviews.

### Skill Routing

- Use `writing-spec` when the work changes or reviews source of truth: current Specs, Drafts, candidate patches, capability boundaries, contracts, invariants, permissions, or source-of-truth drift.
- Use `writing-plan` when the work chooses how to satisfy Specs: implementation strategy, phases, dependency order, orchestration, migrations, rollout, rollback, risk, validation, or task candidates.
- Use `writing-tasks` when the work turns a Plan or clear goal into execution: atomic task cards, dependencies, blockers, acceptance criteria, execution logs, dashboards, inbox triage, or task review.

### Operating Rules

- Current first: read current Specs, active Plans, and the current Task before relying on chat history or archived material.
- Small context cut: load only the Spec, Plan, and Task files needed for the immediate decision.
- No hidden truth: do not bury new APIs, permissions, invariants, or behavioral constraints in Plans or Task logs; update or propose a Spec Patch.
- No strategy in task logs: record execution facts in Tasks, but update Plans when the route, sequencing, rollout, or tradeoffs change.
- No epic tasks: keep Tasks independently executable, retryable, reviewable, and verifiable.
- Review before done: before marking a Task complete, check whether follow-up Tasks, the active Plan, or current Specs need updates.
- Archive is not context: do not replay Patch Logs, old Snapshots, or archived Drafts unless the user asks for history or recovery.

### Writeback Flow

```text
Task discovery -> Plan update -> Spec Patch when needed
```

- If Task execution discovers a route change, update the active Plan.
- If Task execution discovers a system truth change, propose a Spec Patch.
- If Plan work discovers a missing or conflicting source of truth, propose a Spec Patch.
- After Spec changes, review affected Plans and Tasks for invalid assumptions.

### Layer Hooks

- After updating Specs with `writing-spec`, ask whether to create or update an implementation Plan with `writing-plan`.
- After creating or updating a Plan with `writing-plan`, ask whether to create or update executable Tasks with `writing-tasks`.
- These hooks only ask for confirmation; do not create downstream artifacts automatically.

<!-- END: Spec Coding -->
