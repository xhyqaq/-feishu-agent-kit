# {{BOT_NAME}}

这是一个基于 Feishu Agent Kit 生成的机器人项目。

## 目录

- `feishu-runtime/`：飞书运行态工作目录。
- `agent_bot/`：确定性 CLI 工具层。
- `bin/`：cc-connect command/cron shell 入口。
- `config/`：非敏感配置模板。
- `docs/`：运行和权限文档。
- `tests/`：回归测试。

## 本地验证

```bash
python3 -m unittest discover -s tests -v
```
