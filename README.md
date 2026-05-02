# Skill Vault

Curated library of adapted agent skills for our own workflow.

Goal:
- Keep interesting third-party skills in one clean place.
- Normalize them for our usage.
- Publish ready-to-use packs for multiple environments without maintaining four unrelated copies by hand.

## Principles

- `skills/` is the source of truth.
- `dist/` contains generated distributions for specific environments.
- Every adapted skill keeps lightweight source metadata in `skill.yaml`.
- We preserve the useful part of upstream skills and remove repo-specific noise that does not help our usage.

## Current Skills

| ID | What it does | Status | Targets |
|---|---|---|---|
| `caveman` | Compresses agent output while keeping technical accuracy | adapted | Codex, Claude Code, OpenCode, Antigravity |

## Repository Layout

```text
catalog/             Machine-readable index of the library
docs/                Human docs for environments and maintenance
scripts/             Build and validation helpers
skills/              Canonical adapted skills
dist/                Generated target-specific packs
```

## Skill Workflow

1. Find an upstream skill worth keeping.
2. Add source metadata to `skills/<id>/skill.yaml`.
3. Adapt the canonical `skills/<id>/SKILL.md` for our workflow.
4. Run `python scripts/build.py`.
5. Publish or copy the generated pack from `dist/`.

## First Skill

`caveman` started from:
- upstream repo: `JuliusBrussee/caveman`
- upstream path: `skills/caveman`

Our adaptation keeps the core behavior only:
- concise response mode
- compression rules
- safety fallback for ambiguous or destructive situations

Removed from the first-pass library version:
- repo-specific hooks
- installer logic
- stats helpers
- plugin wrappers
- extra companion skills

## Quick Build

```powershell
python .\scripts\build.py
```

## Install Notes

- Codex: copy `dist/codex/skills/<skill-name>` into `~/.codex/skills/`
- Claude Code: copy `dist/claude-code/.claude/skills/<skill-name>` into `~/.claude/skills/`
- OpenCode: copy `dist/opencode/.opencode/skills/<skill-name>` into `.opencode/skills/` or `~/.config/opencode/skills/`
- Antigravity: copy `dist/antigravity/.agents/skills/<skill-name>` into your workspace skill directory

See [docs/environments.md](docs/environments.md) for the current target notes and caveats.
