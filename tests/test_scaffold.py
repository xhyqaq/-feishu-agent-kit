from __future__ import annotations

import subprocess
import tempfile
import unittest
from pathlib import Path


class ScaffoldTests(unittest.TestCase):
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
            self.assertIn("demo-agent", (target / "README.md").read_text(encoding="utf-8"))
            self.assertNotIn("{{BOT_NAME}}", (target / "AGENTS.md").read_text(encoding="utf-8"))

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
