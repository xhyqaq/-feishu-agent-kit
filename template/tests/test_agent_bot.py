from __future__ import annotations

import json
import subprocess
import sys
import unittest
from pathlib import Path


class AgentBotTests(unittest.TestCase):
    def test_check_outputs_card_json(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "agent_bot.cli", "check", "--json"],
            check=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        card = json.loads(result.stdout)
        self.assertEqual(card["schema"], "2.0")
        self.assertIn("检查", card["header"]["title"]["content"])

    def test_runtime_rules_do_not_expose_development_process(self) -> None:
        text = Path("feishu-runtime/AGENTS.md").read_text(encoding="utf-8")

        self.assertNotIn("代码审查", text)
        self.assertNotIn("测试流程", text)
        self.assertIn("飞书交互卡片", text)


if __name__ == "__main__":
    unittest.main()
