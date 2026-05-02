# Skill Vault

Public library of adapted agent skills, kept in one canonical form and published as ready-to-use packs for multiple agent environments.

## What This Repo Is For

- Keep useful third-party skills in one clean public repository.
- Adapt them for our workflow without carrying upstream repo clutter.
- Publish install-ready folders for `Codex`, `Claude Code`, `OpenCode`, `OpenClaw`, and `Antigravity`.

If you want a skill to use immediately, start in `dist/`.
If you want the canonical source we maintain, start in `skills/`.

## Principles

- `skills/` is the source of truth.
- `dist/` contains generated install-ready distributions.
- Each adapted skill records upstream source and license metadata in `skill.yaml`.
- We keep the useful behavior and remove repo-specific noise that does not travel well between environments.

## Current Skills

| ID | What it does | Status | Targets |
|---|---|---|---|
| `caveman` | Compresses agent output while keeping technical accuracy | adapted | Codex, Claude Code, OpenCode, OpenClaw, Antigravity |

## Repository Layout

```text
catalog/             Machine-readable library index
docs/                Human docs for environments and maintenance
scripts/             Build helpers
skills/              Canonical adapted skills
dist/                Generated install-ready packs
```

## Quick Start

Pick the folder that matches your environment and copy the skill directory as-is:

- Codex: `dist/codex/skills/<skill-name>/` -> `~/.codex/skills/<skill-name>/`
- Claude Code: `dist/claude-code/.claude/skills/<skill-name>/` -> `~/.claude/skills/<skill-name>/`
- OpenCode: `dist/opencode/.opencode/skill/<skill-name>/` -> `.opencode/skill/<skill-name>/` or `~/.config/opencode/skill/<skill-name>/`
- OpenClaw: `dist/openclaw/skills/<skill-name>/` -> `<workspace>/skills/<skill-name>/`
- Antigravity: `dist/antigravity/.agents/skills/<skill-name>/` -> your workspace skill directory

Current first skill:

- `caveman`

## First Skill: Caveman

`caveman` started from:

- upstream repo: `JuliusBrussee/caveman`
- upstream path: `skills/caveman`

This repository keeps the portable skill itself and strips out repo-bound extras that are not required to use the skill across different agent runtimes.

Kept in the vault version:

- persistent concise-response mode
- intensity levels
- compression rules
- ambiguity and safety fallback behavior
- examples and activation guidance

Deliberately removed from the public vault copy:

- installer logic
- repo-specific hooks
- stats helpers
- plugin wrappers
- unrelated companion skills

## Maintaining The Vault

1. Add or update `skills/<id>/SKILL.md`.
2. Record source metadata in `skills/<id>/skill.yaml`.
3. Rebuild distributions.
4. Commit both canonical and generated output.

```powershell
python .\scripts\build.py
```

See [docs/environments.md](docs/environments.md) for environment-specific notes.
