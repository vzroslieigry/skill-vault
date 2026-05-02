from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
DIST_DIR = ROOT / "dist"

TARGETS = {
    "codex": DIST_DIR / "codex" / "skills",
    "claude-code": DIST_DIR / "claude-code" / ".claude" / "skills",
    "opencode": DIST_DIR / "opencode" / ".opencode" / "skills",
    "antigravity": DIST_DIR / "antigravity" / ".agents" / "skills",
}


def reset_dist() -> None:
    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)


def copy_skill_tree(source: Path, target: Path) -> None:
    def ignore(_: str, names: list[str]) -> set[str]:
        ignored = {"skill.yaml", "__pycache__"}
        if "overlays" in names:
            ignored.add("overlays")
        return ignored

    shutil.copytree(source, target, ignore=ignore)


def build() -> None:
    reset_dist()

    skill_dirs = [p for p in SKILLS_DIR.iterdir() if p.is_dir() and (p / "SKILL.md").exists()]
    if not skill_dirs:
        raise SystemExit("No skills found in skills/")

    for target_root in TARGETS.values():
        target_root.mkdir(parents=True, exist_ok=True)
        for skill_dir in skill_dirs:
            copy_skill_tree(skill_dir, target_root / skill_dir.name)

    print("Built distributions:")
    for name, path in TARGETS.items():
        print(f"- {name}: {path}")


if __name__ == "__main__":
    build()
