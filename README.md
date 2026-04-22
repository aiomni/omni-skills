# omni-skills

English | [中文](./README.zh-CN.md)

User-focused skills for two common workflows:

- turning vague engineering work into an executable task system
- adding screenshot capture and screenshot-driven testing to `egui` and `eframe` apps

Install any skill in this repository with [`skills.sh`](https://skills.sh/).

## Install with `skills.sh`

Install a single skill:

```bash
npx skills add https://github.com/aiomni/omni-skills --skill egui-screenshot
```

Available skill names:

- `engineering-task-system`
- `egui-screenshot`

> [!NOTE]
> You need `npx` in your shell to run the installation commands.

## Quick Install

If you cloned this repository, install every skill with:

```bash
bash scripts/install-skills.sh
```

If you prefer a one-liner instead of the script:

```bash
REPO="https://github.com/aiomni/omni-skills"
for skill in engineering-task-system egui-screenshot; do
  npx skills add "$REPO" --skill "$skill"
done
```

## Included Skills

### `engineering-task-system`

Turn broad engineering goals into a task system that can actually be executed and reviewed.

Best for:

- breaking work into milestones, dependencies, and a visible critical path
- defining acceptance criteria instead of loose TODO lists
- creating task cards, dashboards, inbox capture, execution logs, and review checkpoints
- keeping task files aligned with the real state of implementation

Install:

```bash
npx skills add https://github.com/aiomni/omni-skills --skill engineering-task-system
```

### `egui-screenshot`

Add, debug, or review screenshot workflows for `egui` and `eframe` applications.

Best for:

- viewport screenshot capture with `ViewportCommand::Screenshot`
- receiving screenshot results from `Event::Screenshot`
- exporting `ColorImage` data to PNG correctly
- adding screenshot-driven tests and visual regression coverage
- exposing screenshots to AI tools or host integrations

Install:

```bash
npx skills add https://github.com/aiomni/omni-skills --skill egui-screenshot
```

## Which Skill Should You Choose?

- Choose `engineering-task-system` when the hard part is planning, sequencing, tracking, or reviewing engineering work.
- Choose `egui-screenshot` when the hard part is capturing UI images, saving screenshots, or testing `egui` output.
- Install both if you want one skill for delivery management and another for UI screenshot workflows.

## Repository Contents

```text
skills/
├── engineering-task-system/
└── egui-screenshot/
```
