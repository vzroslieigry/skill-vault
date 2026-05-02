# Environment Notes

This library keeps one canonical skill and generates environment-specific copies.

Target paths below follow the current official documentation reviewed on May 2, 2026.

## Codex

- Canonical install style in this workspace: `~/.codex/skills/<skill-name>/SKILL.md`
- Vault distribution path: `dist/codex/skills/<skill-name>/`

## Claude Code

- Standard skill layout: `~/.claude/skills/<skill-name>/SKILL.md`
- Vault distribution path: `dist/claude-code/.claude/skills/<skill-name>/`

## OpenCode

- Supported native paths include `.opencode/skill/<skill-name>/SKILL.md` and `~/.config/opencode/skill/<skill-name>/SKILL.md`
- Claude-compatible `.claude/skills/<skill-name>/SKILL.md` paths also work in OpenCode, but we publish a native OpenCode pack
- Vault distribution path: `dist/opencode/.opencode/skill/<skill-name>/`

## OpenClaw

- Supported locations include `<workspace>/skills/<skill-name>/SKILL.md`, `<workspace>/.agents/skills/<skill-name>/SKILL.md`, `~/.agents/skills/<skill-name>/SKILL.md`, and `~/.openclaw/skills/<skill-name>/SKILL.md`
- We publish a workspace-local OpenClaw pack at `dist/openclaw/skills/<skill-name>/`

## Antigravity

- We currently publish a workspace-compatible pack at `dist/antigravity/.agents/skills/<skill-name>/`
- If a local Antigravity setup expects a different root such as `.agent/skills/`, copy the same skill folder there
- Keep Antigravity-specific guidance in repo docs if we standardize on a single install path later
