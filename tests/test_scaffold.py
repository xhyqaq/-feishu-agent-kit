from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


class ScaffoldTests(unittest.TestCase):
    def test_template_repository_has_agent_rules_at_root(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        root_rules = (repo / "AGENTS.md").read_text(encoding="utf-8")

        self.assertIn("模板仓库工作目录", root_rules)
        self.assertIn("template/AGENTS.md", root_rules)
        self.assertIn("template/feishu-runtime/AGENTS.md", root_rules)

    def test_create_bot_generates_runnable_project(self) -> None:
        repo = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "demo-agent"
            subprocess.run(
                [str(repo / "scripts/create-bot.sh"), "demo-agent", str(target)],
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            self.assertTrue((target / "agent-bot").exists())
            self.assertTrue((target / "AGENTS.md").exists())
            self.assertTrue((target / "CLAUDE.md").exists())
            self.assertTrue((target / "feishu-runtime/AGENTS.md").exists())
            self.assertTrue((target / "feishu-runtime/CLAUDE.md").exists())
            self.assertTrue((target / "docs/official-references.md").exists())
            self.assertIn("demo-agent", (target / "README.md").read_text(encoding="utf-8"))
            self.assertEqual("@AGENTS.md\n", (target / "CLAUDE.md").read_text(encoding="utf-8"))
            self.assertEqual("@AGENTS.md\n", (target / "feishu-runtime/CLAUDE.md").read_text(encoding="utf-8"))
            self.assertIn("docs/official-references.md", (target / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertIn("docs/official-references.md", (target / "feishu-runtime/AGENTS.md").read_text(encoding="utf-8"))
            self.assertNotIn("{{BOT_NAME}}", (target / "AGENTS.md").read_text(encoding="utf-8"))
            self.assertNotIn("{{BOT_NAME}}", (target / "feishu-runtime/AGENTS.md").read_text(encoding="utf-8"))

            subprocess.run(
                ["python3", "-m", "unittest", "discover", "-s", "tests", "-v"],
                cwd=target,
                check=True,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )


if __name__ == "__main__":
    unittest.main()
