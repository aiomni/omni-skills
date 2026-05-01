# AGENTS.md

## Project Overview

This repository maintains reusable AI/Codex skills for engineering task management, `egui` screenshot workflows, and Spec System authoring. Skills live under `skills/`, with each skill rooted at `skills/<skill-name>/SKILL.md` and optional `references/`, `assets/`, `scripts/`, or `agents/` subdirectories.

## Language Policy

- Write all skill content descriptions in English, including `description`, `short_description`, marketplace summaries, trigger descriptions, and any other short text whose purpose is to describe when or why a skill should be used.
- Match the user's requested language for all assistant replies, specs, plans, task cards, reviews, generated docs, and other user-facing output.
- If the user's request is in English, reply and write generated artifacts in English.
- If the user's request is in Chinese or another language, reply and write generated artifacts in that same language.
- If the user explicitly asks for a language, or the surrounding context specifies one, that explicit language requirement overrides automatic language matching.
- Keep code identifiers, file paths, CLI commands, API names, and established technical terms in their original form unless the user asks otherwise.
- Do not add skill instructions that hard-code a default response language such as “Chinese first” or “English only”; use this policy instead.

## Skill Authoring Rules

- Keep skill frontmatter valid YAML and include at least `name` and `description`.
- Use English for skill trigger metadata even when the detailed reference material or templates include another language.
- When adding a `Language Policy` section to a skill, make it self-contained for downstream users; do not tell installed skills to follow this repository's `AGENTS.md`.
- Skill-level `Language Policy` sections should only control the language of replies and generated artifacts: English requests get English output, Chinese or other-language requests get matching-language output, and explicit user or context language requirements override automatic matching.
- Make skill trigger descriptions concrete: list the user intents, keywords, and situations that should activate the skill.
- Prefer targeted references over large context dumps; point agents to the smallest relevant `references/` file when possible.
- Keep reusable templates under `assets/templates/` and avoid overwriting a user's existing project structure without checking current conventions first.

## Repository Workflow

- Install all skills from a clone with `bash scripts/install-skills.sh`.
- Install one skill from the published repository with `npx skills add https://github.com/aiomni/omni-skills --skill <skill-name>`.
- Update `README.md` and `README.zh-CN.md` when adding, removing, or renaming skills.
- Preserve the bilingual README structure: `README.md` is English and `README.zh-CN.md` is Chinese.

## Validation

- After editing skill metadata, check descriptions with `rg -n "description:|short_description:" skills`.
- After changing installation behavior, run or inspect `bash scripts/install-skills.sh` as appropriate.
- There is no general test suite in this repository; validate skill changes by checking Markdown/YAML structure and any touched scripts.
