#!/usr/bin/env python3
"""Automated Multi-Harness Skill Test Runner.

Loops over all skills in the central pack and across agent harnesses (Antigravity,
Kiro, Cursor, OpenCode). Tests YAML frontmatter, STE compliance, relative link
resolution, script syntax, and harness discovery.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from pathlib import Path

SKILLS_ROOT = Path.home() / "projects" / "skills" / "skills"
HARNESS_ROOTS = {
    "Antigravity (Agy)": Path.home() / ".gemini" / "config" / "skills",
    "Kiro": Path.home() / ".kiro" / "skills",
    "Cursor": Path.home() / ".cursor" / "skills",
    "OpenCode": Path.home() / ".config" / "opencode" / "skills",
}

FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


class SkillTester:
    def __init__(self, skill_dir: Path):
        self.skill_dir = skill_dir
        self.skill_name = skill_dir.name
        self.skill_file = skill_dir / "SKILL.md"
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.tests_run = 0
        self.tests_passed = 0

    def run_all(self) -> bool:
        self.test_file_exists()
        if not self.skill_file.is_file():
            return False

        content = self.skill_file.read_text(encoding="utf-8", errors="replace")
        self.test_frontmatter(content)
        self.test_link_resolution(content)
        self.test_ste_compliance(content)
        self.test_script_syntax()
        self.test_harness_discovery()
        return len(self.errors) == 0

    def test_file_exists(self):
        self.tests_run += 1
        if not self.skill_file.is_file():
            self.errors.append(f"Missing SKILL.md in {self.skill_dir}")
        else:
            self.tests_passed += 1

    def test_frontmatter(self, content: str):
        self.tests_run += 1
        match = FRONTMATTER_RE.match(content)
        if not match:
            self.errors.append("Missing or invalid YAML frontmatter delimiters (---)")
            return

        fm = match.group(1)
        name_match = re.search(r"(?m)^name:\s*['\"]?([a-zA-Z0-9_-]+)['\"]?", fm)
        if not name_match:
            self.errors.append("Missing 'name' in YAML frontmatter")
        else:
            declared_name = name_match.group(1)
            if declared_name != self.skill_name and self.skill_name != "executive-function":
                self.warnings.append(f"Frontmatter name '{declared_name}' differs from dir '{self.skill_name}'")

        desc_match = re.search(r"(?m)^description:\s*(\S.*)", fm)
        if not desc_match:
            self.errors.append("Missing 'description' in YAML frontmatter")

        if len(self.errors) == 0:
            self.tests_passed += 1

    def test_link_resolution(self, content: str):
        self.tests_run += 1
        broken_links = []
        for match in LINK_RE.finditer(content):
            href = match.group(1).strip()
            if href.startswith(("http://", "https://", "mailto:", "#")):
                continue
            clean_href = href.split("#", 1)[0]
            if not clean_href or clean_href.startswith(("$", "~", "/")):
                continue

            target = (self.skill_dir / clean_href).resolve()
            if not target.exists():
                broken_links.append(clean_href)

        if broken_links:
            self.errors.append(f"Broken relative markdown links: {', '.join(broken_links)}")
        else:
            self.tests_passed += 1

    def test_ste_compliance(self, content: str):
        self.tests_run += 1
        lines = content.splitlines()
        in_code = False
        long_sentences = 0
        for line in lines:
            if line.startswith("```"):
                in_code = not in_code
                continue
            if in_code or line.startswith("|") or not line.strip():
                continue

            sentences = re.split(r"[.!?]\s+", line.strip())
            for s in sentences:
                words = s.split()
                if len(words) > 40:
                    long_sentences += 1

        if long_sentences > 3:
            self.warnings.append(f"{long_sentences} sentences exceed 40 words")
        self.tests_passed += 1

    def test_script_syntax(self):
        self.tests_run += 1
        scripts = list(self.skill_dir.rglob("*.sh"))
        script_errors = []
        for script in scripts:
            res = subprocess.run(["bash", "-n", str(script)], capture_output=True, text=True)
            if res.returncode != 0:
                script_errors.append(f"{script.name}: {res.stderr.strip()}")

        if script_errors:
            self.errors.append(f"Script syntax errors: {'; '.join(script_errors)}")
        else:
            self.tests_passed += 1

    def test_harness_discovery(self):
        self.tests_run += 1
        missing_harnesses = []
        for harness_name, harness_path in HARNESS_ROOTS.items():
            if not harness_path.exists():
                continue
            target = harness_path / self.skill_name
            if not target.exists():
                if self.skill_name == "executive-function" and (harness_path / "ef-starter").exists():
                    continue
                missing_harnesses.append(harness_name)

        if missing_harnesses:
            self.warnings.append(f"Not symlinked in: {', '.join(missing_harnesses)}")
        self.tests_passed += 1


def main() -> int:
    if not SKILLS_ROOT.is_dir():
        print(f"FAIL: Skills root not found at {SKILLS_ROOT}", file=sys.stderr)
        return 1

    skill_dirs = sorted([d for d in SKILLS_ROOT.iterdir() if d.is_dir()])
    print(f"=== Running Skill Test Loop ({len(skill_dirs)} skills) ===\n")

    total_skills = len(skill_dirs)
    passed_skills = 0
    total_tests = 0
    total_passed_tests = 0

    for idx, skill_dir in enumerate(skill_dirs, 1):
        tester = SkillTester(skill_dir)
        ok = tester.run_all()
        total_tests += tester.tests_run
        total_passed_tests += tester.tests_passed

        status_icon = "PASS" if ok else "FAIL"
        print(f"[{idx:02d}/{total_skills:02d}] {status_icon}: {tester.skill_name:<32} ({tester.tests_passed}/{tester.tests_run} checks passed)")

        for err in tester.errors:
            print(f"     ERROR: {err}")
        for warn in tester.warnings:
            print(f"     WARN:  {warn}")

        if ok:
            passed_skills += 1

    print("\n" + "=" * 50)
    print(f"Summary: {passed_skills}/{total_skills} skills passed ({total_passed_tests}/{total_tests} total checks)")

    return 0 if passed_skills == total_skills else 1


if __name__ == "__main__":
    sys.exit(main())
