#!/usr/bin/env python3
"""Validate the public health-r-project-scaffold release package."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "health-r-project-scaffold"

FORBIDDEN_TEXT = [
    "C" + ":/",
    "C" + ":\\\\",
    "D" + ":/",
    "D" + ":\\\\",
    "Z" + ":/",
    "Z" + ":\\\\",
    "tsukuba" + "-internship",
    "server" + "_all" + "_installed",
    "Definition" + "_of" + "_Tsukuba",
    "zip" + "_add" + "_for" + "_lab",
]

FORBIDDEN_EXTENSIONS = {
    ".dta",
    ".sas7bdat",
    ".sas7bcat",
    ".sav",
    ".por",
    ".xlsx",
    ".rds",
}

MAX_PUBLIC_FILE_BYTES = 1_000_000


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def iter_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def check_required_files() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "INSTALL.md",
        ROOT / "CHANGELOG.md",
        ROOT / "LICENSE",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "output_contract.md",
        SKILL / "references" / "decision_algorithm.md",
        SKILL / "assets" / "templates" / "project.yml.template",
    ]
    missing = [str(path.relative_to(ROOT)) for path in required if not path.exists()]
    if missing:
        fail("Missing required files: " + ", ".join(missing))


def check_skill_frontmatter() -> None:
    text = read_text(SKILL / "SKILL.md")
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    frontmatter = text.split("---", 2)[1]
    if not re.search(r"^name:\s*health-r-project-scaffold\s*$", frontmatter, re.M):
        fail("SKILL.md frontmatter name is missing or wrong")
    if not re.search(r"^description:\s*.+", frontmatter, re.M):
        fail("SKILL.md frontmatter description is missing")
    if text.count("---") < 2:
        fail("SKILL.md frontmatter is not closed")


def check_openai_yaml() -> None:
    text = read_text(SKILL / "agents" / "openai.yaml")
    required = [
        'display_name: "Health R Project Scaffold"',
        'short_description: "Scaffold auditable R health projects"',
        'default_prompt: "Use $health-r-project-scaffold',
    ]
    missing = [item for item in required if item not in text]
    if missing:
        fail("agents/openai.yaml missing expected interface fields")


def check_public_safety() -> None:
    files = iter_files()
    bad_ext = [path for path in files if path.suffix.lower() in FORBIDDEN_EXTENSIONS]
    if bad_ext:
        fail("Forbidden raw/binary evidence files found: " + ", ".join(str(p.relative_to(ROOT)) for p in bad_ext))
    large = [path for path in files if path.stat().st_size > MAX_PUBLIC_FILE_BYTES]
    if large:
        fail("Unexpected large public files found: " + ", ".join(str(p.relative_to(ROOT)) for p in large))
    text_suffixes = {".md", ".txt", ".csv", ".yml", ".yaml", ".html", ".template", ".R", ".py", ".gitignore", ".gitattributes"}
    matches: list[str] = []
    for path in files:
        if path.suffix not in text_suffixes and path.name not in {".gitignore", ".gitattributes", "LICENSE"}:
            continue
        content = read_text(path)
        for pattern in FORBIDDEN_TEXT:
            if re.search(pattern, content):
                matches.append(f"{path.relative_to(ROOT)} contains {pattern}")
    if matches:
        fail("Forbidden local/private markers found: " + "; ".join(matches))


def check_install_docs() -> None:
    text = read_text(ROOT / "INSTALL.md")
    if "install-skill-from-github.py" not in text:
        fail("INSTALL.md must document skill-installer GitHub installation")
    if "$HOME\\.codex\\skills\\health-r-project-scaffold" not in text:
        fail("INSTALL.md must document local Codex skill installation path")


def main() -> int:
    check_required_files()
    check_skill_frontmatter()
    check_openai_yaml()
    check_public_safety()
    check_install_docs()
    print("PASS: public release validation checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
