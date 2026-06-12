# 官方规范索引

本文记录开发本飞书 Agent 机器人时应优先查阅的官方文档和上游项目文档。涉及消息格式、卡片结构、回调、权限、cc-connect 配置或 Agent 运行方式时，不要只凭记忆实现；先打开对应文档确认当前语法和限制。

## 飞书 / Lark

- 发送消息 API：https://open.feishu.cn/document/server-docs/im-v1/message/create?lang=zh-CN
- 发送消息内容结构：https://open.feishu.cn/document/server-docs/im-v1/message-content-description/create_json?lang=zh-CN
- 飞书卡片概览：https://open.feishu.cn/document/feishu-cards/feishu-card-overview?lang=zh-CN
- Card JSON 2.0 结构：https://open.feishu.cn/document/feishu-cards/card-json-v2-structure?lang=zh-CN
- Card JSON 2.0 组件：https://open.feishu.cn/document/feishu-cards/card-json-v2-components/component-json-v2-overview?lang=zh-CN
- Card JSON 2.0 版本变更：https://open.feishu.cn/document/feishu-cards/card-json-v2-breaking-changes-release-notes?lang=zh-CN
- 卡片搭建工具：https://open.feishu.cn/document/tools-and-resources/message-card-builder?lang=zh-CN
- 卡片回调通信结构：https://open.larksuite.com/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/card-callback-communication
- 处理卡片回调：https://open.larksuite.com/document/uAjLw4CM/ukzMukzMukzM/feishu-cards/handle-card-callbacks
- 回调订阅概览：https://open.larksuite.com/document/uAjLw4CM/ukTMukTMukTM/event-subscription-guide/callback-subscription/callback-overview

## cc-connect

- GitHub 仓库：https://github.com/chenhg5/cc-connect
- 安装和配置：https://github.com/chenhg5/cc-connect/blob/main/INSTALL.md
- 使用指南：https://github.com/chenhg5/cc-connect/blob/main/docs/usage.md
- 配置模板：https://github.com/chenhg5/cc-connect/blob/main/config.example.toml

## Agent 工具

- Codex：https://developers.openai.com/codex/
- Claude Code：https://docs.anthropic.com/claude-code

## 使用规则

- 修改飞书消息发送、消息类型、卡片 JSON、卡片按钮或回调逻辑前，先查本文件对应官方文档。
- 如果官方文档与项目模板冲突，以官方文档为准，再更新模板和测试。
- 不要把第三方博客当作唯一依据；博客只能作为经验参考，最终以官方文档和上游项目文档为准。
