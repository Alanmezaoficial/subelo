#!/usr/bin/env python3
# Copyright (c) 2026 Enrique Rocha (@soyenriquerocha)
# SPDX-License-Identifier: MIT
# id: er-587bf42d
"""
Build the release assets.

Two archives, two different shapes — this is the part that is easy to get
wrong by hand, which is why it lives in a script:

  subelo.skill        zip, everything nested under an `subelo/` folder
                          (matches the v0.1.0 asset layout)
  subelo-web.plugin  zip, contents at the archive root, per the Cowork
                          plugin format

Neither includes README, CONTRIBUTING, tests, docs or CI config — those are
for people reading the repo, not for the installed skill.

Usage:
    package_skill.py [--out DIR]     # default: dist/
"""

import argparse
import shutil
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_NAME = "subelo"
SKILL_ROOT = REPO / "claude" / "skills" / "subelo"

# Scripts that are repo maintenance, not part of the installed skill.
SCRIPT_EXCLUDES = {"package_skill.py", "sync_cowork_plugin.py"}
NOISE = {".DS_Store"}


def skill_files() -> list[Path]:
    files = [SKILL_ROOT / "SKILL.md", SKILL_ROOT / "LICENSE", SKILL_ROOT / "NOTICE"]
    files += sorted(SKILL_ROOT.glob("references/**/*.md"))
    files += sorted(p for p in SKILL_ROOT.glob("scripts/*.py") if p.name not in SCRIPT_EXCLUDES)
    files += sorted(p for p in SKILL_ROOT.glob("assets/**/*") if p.is_file() and p.name not in NOISE)
    return files


def build_skill(out: Path) -> Path:
    target = out / f"{SKILL_NAME}.skill"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for path in skill_files():
            z.write(path, f"{SKILL_NAME}/{path.relative_to(SKILL_ROOT).as_posix()}")
    return target


def build_plugin(out: Path) -> Path:
    root = REPO / "claude" / "cowork-plugin"
    name = "subelo-web"
    target = out / f"{name}.plugin"
    with zipfile.ZipFile(target, "w", zipfile.ZIP_DEFLATED) as z:
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.name in NOISE:
                continue
            z.write(path, path.relative_to(root).as_posix())
    return target


def verify_skill(archive: Path) -> bool:
    """Extract and run the repo's own validator against it. A release asset
    that is missing a reference file is worse than no release asset."""
    with tempfile.TemporaryDirectory() as tmp:
        with zipfile.ZipFile(archive) as z:
            z.extractall(tmp)
        result = subprocess.run(
            [sys.executable, str(REPO / "tests" / "claude" / "validate_skill.py"), str(Path(tmp) / SKILL_NAME)],
            capture_output=True, text=True,
        )
        print(f"  {result.stdout.strip() or result.stderr.strip()}")
        return result.returncode == 0


def verify_plugin(archive: Path) -> bool:
    with zipfile.ZipFile(archive) as z:
        names = set(z.namelist())
    required = {".claude-plugin/plugin.json", "skills/subelo-web/SKILL.md"}
    missing = required - names
    if missing:
        print(f"  FAIL — missing from plugin: {', '.join(sorted(missing))}")
        return False
    print(f"  PASS — plugin valid, {len(names)} files")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(epilog='Hecho por Enrique Rocha (@soyenriquerocha) · tododeia.com', description="Build release assets")
    parser.add_argument("--out", default=str(REPO / "dist"))
    args = parser.parse_args()

    out = Path(args.out)
    out = out.resolve()
    if out == REPO or REPO not in out.parents:
        raise SystemExit("Output must be a new directory inside this repository")
    if out.exists():
        raise SystemExit("Output exists; choose a new directory, nothing was removed")
    out.mkdir(parents=True)

    ok = True
    for build, verify in ((build_skill, verify_skill), (build_plugin, verify_plugin)):
        archive = build(out)
        print(f"{archive.relative_to(REPO) if archive.is_relative_to(REPO) else archive}  "
              f"({archive.stat().st_size / 1024:.0f} KB)")
        ok &= verify(archive)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
