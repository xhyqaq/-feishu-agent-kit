# Feishu Agent Bot Template

这是一个用于沉淀和复制飞书 Agent 机器人的项目模板。它来自 `server-monitor-agent` 的已上线实践，但抽掉了具体业务实现，保留通用架构、运行规范、权限边界和可生成的新机器人骨架。

## 产物层次

- 技术规范文档：定义机器人应遵守的架构、安全和交互标准。
- 项目模板：提供一个新机器人项目的推荐目录、运行入口和规则文件。
- 脚手架：用 `scripts/create-bot.sh` 从模板生成一个新机器人目录。

## 快速生成

```bash
./scripts/create-bot.sh my-agent-bot /Users/xhy/Project/my-agent-bot
```

生成后：

```bash
cd /Users/xhy/Project/my-agent-bot
python3 -m unittest discover -s tests -v
```

## 核心原则

- 飞书是交互载体，不是命令行窗口。
- 用户可见结果优先使用飞书 Card JSON 2.0。
- 确定性逻辑放进 CLI 和 shell wrapper。
- 自然语言理解由 Agent 负责，但写操作必须有确认、验证和审计。
- `work_dir` 和 `AGENTS.md` 是行为约束，不是 OS 安全边界。
- 生产部署必须设计独立的文件权限、用户权限和容器挂载边界。

## 文档

- [技术规范](docs/technical-standard.md)
- [项目模板说明](docs/project-template.md)
- [运行权限模型](docs/runtime-permissions.md)
