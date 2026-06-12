# 项目模板说明

本模板生成的新机器人项目采用以下结构：

```text
bot-project/
  AGENTS.md
  README.md
  agent-bot
  agent_bot/
    __init__.py
    cli.py
    cards.py
  bin/
    runtime-env.sh
    manual-check.sh
    scheduled-check.sh
    ops-action.sh
  config/
    targets.example.toml
  docs/
    official-references.md
    runtime-permissions.md
  feishu-runtime/
    AGENTS.md
  tests/
    test_agent_bot.py
```

## 目录职责

- `AGENTS.md`：开发目录规则，说明这里不是飞书用户对话目录。
- `feishu-runtime/AGENTS.md`：飞书运行态规则，约束 Agent 面向用户时如何说话和做事。
- `agent_bot/`：确定性工具层。
- `bin/`：`cc-connect command/cron` 的 shell 入口。
- `config/`：非敏感配置模板。
- `docs/`：部署、权限和架构文档。
- `docs/official-references.md`：飞书/Lark、cc-connect 和 Agent 工具的官方文档索引，供 AI 开发时查证规范。
- `tests/`：回归测试。

## cc-connect 配置示例

```toml
[[projects]]
name = "my-agent-bot"
reply_footer = false
reset_on_idle_mins = 30

[projects.agent]
type = "codex"

[projects.agent.options]
work_dir = "/opt/cc-connect/projects/my-agent-bot/feishu-runtime"
mode = "yolo"

[[projects.platforms]]
type = "feishu"

[projects.platforms.options]
app_id = "cli_xxx"
app_secret = "env-or-secret"
allow_from = "ou_xxx"
enable_feishu_card = true
reply_to_trigger = false
progress_style = "card"

[projects.display]
tool_messages = false

[[commands]]
name = "check"
exec = "/opt/cc-connect/projects/my-agent-bot/bin/manual-check.sh"

[[commands]]
name = "ops-action"
exec = "/opt/cc-connect/projects/my-agent-bot/bin/ops-action.sh {{args}}"
```

生产环境中，`exec` 推荐指向 root 拥有的降权启动器，而不是直接执行项目可写脚本。

## 新机器人落地步骤

1. 用脚手架生成项目。
2. 修改 `README.md`、`AGENTS.md` 和 `feishu-runtime/AGENTS.md`，明确机器人能力边界。
3. 在 `config/targets.example.toml` 中定义非敏感目标。
4. 在 `agent_bot/cli.py` 中实现业务检查和动作。
5. 在 `agent_bot/cards.py` 中实现用户可见卡片。
6. 添加测试，确保卡片不泄露内部字段。
7. 配置 cc-connect project、commands 和 cron。
8. 配置 OS 用户、目录权限和容器挂载边界。
9. 用真实环境做只读验证。
10. 再开启主动推送和写操作。
