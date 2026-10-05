"""Installer integration tests. All writes stay in temporary HOME/repository fixtures."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

APPLY = Path(__file__).resolve().parents[1] / "apply"


class ApplyTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.repo = self.root / "repo"
        self.repo.mkdir()
        shutil.copy2(APPLY, self.repo / "apply")
        self.source = self.repo / "skills" / "sample"
        self.source.mkdir(parents=True)
        (self.source / "SKILL.md").write_text("---\nname: sample\ndescription: Test\n---\nSee references/guide.md\n")
        (self.source / "references").mkdir()
        (self.source / "references" / "guide.md").write_text("portable\n")
        for name in ("AGENTS.md", "harness-context.md", "GEMINI.md"):
            (self.repo / name).write_text("repository guidance\n")
        self.env = dict(os.environ, HOME=str(self.home), SKIP_KARLO_SYNC="1")
        self.env.pop("HERMES_HOME", None)

    def run_apply(self, *args, success=True):
        result = subprocess.run([str(self.repo / "apply"), "-y", *args], env=self.env,
                                text=True, capture_output=True)
        if success:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0)
        return result

    def test_foreign_skills_guidance_and_config_survive(self):
        target = self.home / ".agents"
        skills = target / "skills"
        skills.mkdir(parents=True)
        (skills / "broken").symlink_to("/missing/foreign")
        (skills / "sample").symlink_to("/missing/sample")
        (skills / "speckit").mkdir()
        (skills / "speckit" / "keep").write_text("foreign")
        (target / "AGENTS.md").write_text("my rules")
        (target / "skills.json").write_text("my config")
        (target / "enabled-skills").mkdir()
        self.run_apply()
        self.assertTrue((skills / "broken").is_symlink())
        self.assertEqual(os.readlink(skills / "sample"), "/missing/sample")
        self.assertEqual((skills / "speckit" / "keep").read_text(), "foreign")
        self.assertEqual((target / "AGENTS.md").read_text(), "my rules")
        self.assertEqual((target / "skills.json").read_text(), "my config")
        self.assertTrue((target / "enabled-skills").is_dir())

    def test_hermes_copies_are_idempotent_and_targeted(self):
        self.run_apply("--harness", "hermes")
        target = self.home / ".hermes"
        installed = target / "skills/sample"
        self.assertTrue(installed.is_dir())
        self.assertFalse(installed.is_symlink())
        self.assertEqual((installed / "references/guide.md").read_text(), "portable\n")
        manifest = target / "skills/.skills-apply-manifest.json"
        first = manifest.read_bytes()
        stamp = (installed / "SKILL.md").stat().st_mtime_ns
        self.run_apply("--harness=hermes")
        self.assertEqual(manifest.read_bytes(), first)
        self.assertEqual((installed / "SKILL.md").stat().st_mtime_ns, stamp)
        # Targeted runs must not touch unrelated harness directories.
        self.assertFalse((self.home / ".agents").exists())
        # Hermes copies live alongside its own skills; no repo guidance is injected.
        self.assertFalse((target / "AGENTS.md").exists())
        self.assertNotIn(str(self.repo), manifest.read_text())

    def test_hermes_home_override_and_foreign_preservation(self):
        hermes = self.root / "custom-hermes"
        skill_root = hermes / "skills"
        skill_root.mkdir(parents=True)
        (skill_root / "foreign").mkdir()
        (skill_root / "foreign" / "own.md").write_text("mine\n")
        (skill_root / "sample").write_text("not a directory\n")
        foreign_link = skill_root / "sample-link"
        foreign_link.symlink_to("/missing/foreign")
        self.env["HERMES_HOME"] = str(hermes)
        self.run_apply("--harness", "hermes")
        self.assertEqual((skill_root / "foreign" / "own.md").read_text(), "mine\n")
        self.assertEqual((skill_root / "sample").read_text(), "not a directory\n")
        self.assertEqual(os.readlink(foreign_link), "/missing/foreign")
        self.assertTrue((skill_root / "sample" / "SKILL.md").is_file() is False)
        manifest = json.loads((skill_root / ".skills-apply-manifest.json").read_text())["skills"]
        self.assertEqual(manifest, [])
        self.assertFalse(self.home.joinpath(".hermes/skills").exists())


if __name__ == "__main__":
    unittest.main()
