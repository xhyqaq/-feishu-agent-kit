# 官方规范索引

本文记录开发飞书 Agent 机器人时应优先查阅的官方文档和上游项目文档。涉及消息格式、卡片结构、回调、权限、cc-connect 配置或 Agent 运行方式时，不要只凭记忆实现；先打开对应文档确认当前语法和限制。

## 飞书 / Lark

**发送消息 API**

- 中文文档：https://open.feishu.cn/document/server-docs/im-v1/message/create?lang=zh-CN
- 适用场景：调用飞书 OpenAPI 主动发送消息，确认 `receive_id_type`、`msg_type`、`content` 结构、权限和错误码。

**发送消息内容结构**

- 中文文档：https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create_json?lang=zh-CN
- 适用场景：编写文本、富文本、图片、文件、交互卡片等不同 `msg_type` 的 `content` JSON。

**飞书卡片概览**

- 中文文档：https://open.feishu.cn/document/feishu-cards/feishu-card-overview?lang=zh-CN
- 适用场景：确认卡片能力边界、适用场景、客户端兼容性和基本概念。

**Card JSON 2.0 结构**

- 中文文档：https://open.feishu.cn/document/feishu-cards/card-json-v2-structure?lang=zh-CN
- 适用场景：编写 Card JSON 2.0 顶层结构、`schema`、`config`、`header`、`body` 和国际化字段。

**Card JSON 2.0 组件**

- 中文文档：https://open.feishu.cn/document/feishu-cards/card-json-v2-components/component-json-v2-overview?lang=zh-CN
- 适用场景：编写按钮、表格、容器、Markdown、图片等卡片组件。

**Card JSON 2.0 版本变更**

- 中文文档：https://open.feishu.cn/document/feishu-cards/card-json-v2-breaking-changes-release-notes?lang=zh-CN
- 适用场景：从旧版卡片迁移、排查字段不兼容、确认 1.0 和 2.0 的差异。

**卡片搭建工具**

- 中文文档：https://open.feishu.cn/document/tools-and-resources/message-card-builder?lang=zh-CN
- 适用场景：验证卡片结构、快速生成示例、对照官方可视化构建结果。

**卡片回调通信结构**

- Lark 文档：https://open.larksuite.com/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-callback-communication
- 适用场景：处理交互卡片按钮、表单等组件回调，确认回调请求和响应结构。

**处理卡片回调**

- Lark 文档：https://open.larksuite.com/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/handle-card-callbacks
- 适用场景：实现卡片交互回调接收、校验、响应和错误处理。

**回调订阅概览**

- Lark 文档：https://open.larksuite.com/document/uAjLw4CM/ukTMukTMukTM/event-subscription-guide/callback-subscription/callback-overview
- 适用场景：理解飞书/Lark 事件回调与同步回调的区别。

## cc-connect

**GitHub 仓库**

- https://github.com/chenhg5/cc-connect
- 适用场景：确认项目能力、支持的平台、支持的 Agent 类型和最新变更。

**安装和配置**

- https://github.com/chenhg5/cc-connect/blob/main/INSTALL.md
- 适用场景：安装 cc-connect、配置飞书机器人、选择 Agent、配置 project 和 platform。

**使用指南**

- https://github.com/chenhg5/cc-connect/blob/main/docs/usage.md
- 适用场景：确认 command、cron、session、work_dir、附件、TTS、权限模式等行为。

**配置模板**

- https://github.com/chenhg5/cc-connect/blob/main/config.example.toml
- 适用场景：编写或升级 `config.toml`，确认字段名、层级和默认值。

## Agent 工具

**Codex**

- 官方文档：https://developers.openai.com/codex/
- 适用场景：确认 Codex CLI、sandbox、approval、workdir、AGENTS.md、MCP、插件和运行限制。

**Claude Code**

- 官方文档：https://docs.anthropic.com/claude-code
- 适用场景：确认 Claude Code 的项目规则、工具权限、hooks、MCP 和运行方式。

## 使用规则

- 修改飞书消息发送、消息类型、卡片 JSON、卡片按钮或回调逻辑前，先查本文件对应官方文档。
- 如果官方文档与本仓库模板冲突，以官方文档为准，再更新模板和测试。
- 文档链接可能更新；如果链接失效，应从飞书开放平台或 Lark Developer 搜索同名文档并更新本文件。
- 不要把第三方博客当作唯一依据；博客只能作为经验参考，最终以官方文档和上游项目文档为准。
