# Environment Notes

This library keeps one canonical skill and generates environment-specific copies.

## Codex

- Canonical install style in this workspace: `~/.codex/skills/<skill-name>/SKILL.md`
- Vault distribution path: `dist/codex/skills/<skill-name>/`

## Claude Code

- Standard skill layout: `~/.claude/skills/<skill-name>/SKILL.md`
- Vault distribution path: `dist/claude-code/.claude/skills/<skill-name>/`

## OpenCode

- Supported paths include `.opencode/skills/<skill-name>/SKILL.md`
- Claude-compatible `.claude/skills/` paths also work in OpenCode, but we publish a native OpenCode pack
- Vault distribution path: `dist/opencode/.opencode/skills/<skill-name>/`

## Antigravity

- We currently publish a workspace-compatible pack at `dist/antigravity/.agents/skills/<skill-name>/`
- If a local Antigravity setup expects a different root such as `.agent/skills/`, copy the same skill folder there
- Keep Antigravity-specific guidance in repo docs if we standardize on a single install path later
