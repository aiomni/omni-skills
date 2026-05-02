#!/usr/bin/env python3
"""Sync the Spec Coding managed block into a target project's AGENTS.md."""

from __future__ import annotations

import argparse
from pathlib import Path


BEGIN = "<!-- BEGIN: Spec Coding -->"
END = "<!-- END: Spec Coding -->"


def skill_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_template_path() -> Path:
    return skill_root() / "assets" / "templates" / "spec-coding-agents-section.md"


def resolve_agents_path(target: Path) -> Path:
    target = target.resolve()
    if target.name == "AGENTS.md":
        return target
    return target / "AGENTS.md"


def looks_like_omni_skills_repo(project_root: Path) -> bool:
    return (
        (project_root / "SPEC-CODING.md").exists()
        and (project_root / "skills" / "omni-writing-agentsmd" / "SKILL.md").exists()
        and (project_root / "scripts" / "install-skills.sh").exists()
    )


def normalize_block(block: str) -> str:
    block = block.strip()
    if BEGIN not in block or END not in block:
        raise ValueError(f"Template must contain both {BEGIN!r} and {END!r}")
    return block + "\n"


def merge_content(existing: str, block: str) -> str:
    if BEGIN in existing or END in existing:
        if BEGIN not in existing or END not in existing:
            raise ValueError("AGENTS.md has an incomplete Spec Coding managed block")
        start = existing.index(BEGIN)
        end = existing.index(END, start) + len(END)
        merged = existing[:start].rstrip() + "\n\n" + block.rstrip() + "\n" + existing[end:].lstrip()
        return merged.rstrip() + "\n"

    if not existing.strip():
        return "# AGENTS.md\n\n" + block

    return existing.rstrip() + "\n\n" + block


def sync_agents(target: Path, template: Path, allow_omni_skills: bool) -> Path:
    agents_path = resolve_agents_path(target)
    project_root = agents_path.parent

    if looks_like_omni_skills_repo(project_root) and not allow_omni_skills:
        raise SystemExit(
            "Refusing to edit the omni-skills repository AGENTS.md. "
            "Pass the real target project path, or use --allow-omni-skills if this is intentional."
        )

    block = normalize_block(template.read_text(encoding="utf-8"))
    existing = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    agents_path.write_text(merge_content(existing, block), encoding="utf-8")
    return agents_path


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", type=Path, help="Target project root or AGENTS.md path")
    parser.add_argument(
        "--template",
        type=Path,
        default=default_template_path(),
        help="Managed block template path",
    )
    parser.add_argument(
        "--allow-omni-skills",
        action="store_true",
        help="Allow editing this omni-skills repository AGENTS.md when explicitly intended",
    )
    args = parser.parse_args()

    agents_path = sync_agents(args.target, args.template, args.allow_omni_skills)
    print(f"Updated {agents_path}")


if __name__ == "__main__":
    main()
