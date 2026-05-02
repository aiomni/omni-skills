---
name: omni-writing-agentsmd
description: Create or update a target project's AGENTS.md with Spec Coding operating rules after writing-spec, writing-plan, and writing-tasks are installed. Use when the user asks to install, sync, generate, patch, review, or maintain project-level AGENTS.md instructions for Spec Coding, AI coding workflows, source-of-truth Specs, Plans, Tasks, upward writeback, context hygiene, or multi-agent coordination. Do not use this to edit the omni-skills repository AGENTS.md unless that repository is explicitly the user's target project.
---

# Omni Writing AGENTS.md

Use this skill to make a user's project-level `AGENTS.md` teach future AI agents how to work with the `writing-spec`, `writing-plan`, and `writing-tasks` skills as a coherent Spec Coding workflow.

## Target Boundary

- Edit the target user's project `AGENTS.md`.
- If the current working directory is this skill repository, ask the user for the real target project path before writing files.
- Prefer the target repository root `AGENTS.md`. Only edit nested `AGENTS.md` files when the user asks for scope-specific rules.
- Preserve existing project-specific instructions, command conventions, safety rules, and nested `AGENTS.md` precedence.
- Treat direct user instructions and narrower-scope `AGENTS.md` files as higher priority than the generic Spec Coding section.

## Preconditions

- This skill is intended for projects that use the full Spec Coding set: `writing-spec`, `writing-plan`, and `writing-tasks`.
- If one of those skills is obviously missing, tell the user which skill to install and continue only if they still want a preparatory `AGENTS.md` section.
- Do not assume the target project already has `omni-coding/`. Add AGENTS rules that are compatible with creating it later.

## Workflow

1. Identify the target project root from the user's request, otherwise use `git rev-parse --show-toplevel` or the current working directory.
2. Read the target `AGENTS.md` if it exists; otherwise create one at the project root.
3. Prefer running `python3 scripts/sync_spec_coding_agents.py <target-project-root>` to insert or replace the managed block.
4. If editing manually, insert or replace only the block delimited by `<!-- BEGIN: Spec Coding -->` and `<!-- END: Spec Coding -->`.
5. Use `assets/templates/spec-coding-agents-section.md` as the default block content, adapting paths only when the target project already uses different Spec, Plan, or Task locations.
6. Keep the section concise enough for agents to load by default; move long rationale or onboarding material to project docs instead of `AGENTS.md`.
7. After writing, summarize the changed file path and remind the user that the section controls future agents in that target project.

## Script

Use the bundled script for deterministic updates:

```bash
python3 scripts/sync_spec_coding_agents.py /path/to/target-project
```

The script:
- Creates `AGENTS.md` when missing.
- Replaces the existing Spec Coding managed block when present.
- Appends the managed block when `AGENTS.md` has no Spec Coding section.
- Refuses to edit the `omni-skills` repository unless `--allow-omni-skills` is passed.

## Managed Block Requirements

The `AGENTS.md` block must encode these rules:

- `Spec -> Plan -> Task`: `Spec` is source of truth, `Plan` is strategy and path, `Task` is the current execution unit.
- Current first: agents read current Specs, active Plans, and current Tasks before historical archives, logs, or chat history.
- Small context cut: agents load only the relevant Spec, Plan, and Task subset for the immediate work.
- No hidden truth: new interfaces, permissions, invariants, and behavioral constraints belong in Specs, not only in Plans or Task logs.
- No strategy in task logs: route changes update Plans; truth changes propose Spec Patches.
- No epic tasks: Tasks must be independently executable, retryable, reviewable, and verifiable.
- Review before done: task completion includes checking whether downstream Tasks, Plans, or Specs need updates.
- Upward writeback: `Task discovery -> Plan update -> Spec Patch when needed`.
- Layer hooks: after Spec work, ask whether to create or update a Plan; after Plan work, ask whether to create or update Tasks.
