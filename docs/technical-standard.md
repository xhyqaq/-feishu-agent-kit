# 飞书 Agent 机器人技术规范

本文定义可复制的飞书 Agent 机器人技术标准。它面向开发者和维护者，不是飞书用户可见文案。

## 目标

- 飞书只负责交互入口、卡片承载和按钮回调。
- `cc-connect` 负责把飞书消息桥接到本地或服务器上的 Agent、命令和 cron。
- 确定性任务由 CLI 和 shell wrapper 执行，保证可重复、可测试、可审计。
- Agent 负责自然语言理解、复杂排查、代码修改和需要推理的分析。
- 高风险写操作必须走预览、确认、执行、验证、审计流程。

## 分层

```text
Feishu 用户
  |
  v
cc-connect
  |
  +-- commands / cron -> bin/*.sh -> project CLI
  |
  +-- natural language -> Codex Agent -> project work_dir
  |
  v
机器人项目
  - config: 非敏感配置
  - agent_bot: 确定性工具层
  - feishu-runtime: 飞书运行态规则
  - docs: 架构、部署和权限文档
  - tests: 回归测试
```

## 确定性工具层

每个机器人应提供一个项目 CLI，例如：

```bash
./agent-bot check --json
./agent-bot send-card --card-file <path> --yes
./agent-bot action --payload <payload>
```

CLI 负责：

- 读取非敏感配置。
- 调用确定性数据源。
- 生成结构化结果。
- 渲染飞书卡片。
- 执行已注册动作。
- 记录审计日志。

CLI 不负责：

- 自然语言意图理解。
- 自由拼接高风险 shell 命令。
- 把内部字段直接展示给用户。
- 保存密钥或账号凭据。

## 运行态规则

每个项目必须区分开发目录和飞书运行目录。

开发目录用于：

- 开发代码。
- 跑测试。
- 写规范和架构文档。
- 审查变更。

运行目录用于：

- 接收飞书用户自然语言。
- 调用项目 CLI。
- 发送用户可见卡片。
- 处理按钮回调。

运行态 `AGENTS.md` 只能描述用户可见能力和安全边界，不应暴露开发流程、测试流程、内部实现过程或敏感路径。

## 飞书卡片规范

用户可见运维或业务结果优先使用飞书 Card JSON 2.0：

修改飞书消息发送、消息类型、卡片 JSON、卡片按钮或回调逻辑前，必须先查看 [official-references.md](official-references.md) 中的飞书/Lark 官方文档链接，确认当前字段结构、组件语法和回调协议。

```json
{
  "schema": "2.0",
  "header": {
    "title": {"tag": "plain_text", "content": "结果标题"}
  },
  "body": {
    "elements": []
  }
}
```

按钮回调应使用安全引用：

```json
{
  "tag": "button",
  "text": {"tag": "plain_text", "content": "确认"},
  "type": "default",
  "width": "default",
  "behaviors": [
    {"type": "callback", "value": {"action": "cmd:/ops-action action_id=change.apply token=..."}}
  ]
}
```

禁止在用户可见内容中出现：

- API key、token、密码、账号凭据。
- 原始接口响应。
- 内部事件 ID、fingerprint、raw metric 字段名。
- 大段 shell stdout/stderr。
- 开发过程、测试过程、技术实现解释。

## 主动任务规范

定时任务必须是确定性 `exec`，不要把分钟级任务做成每分钟启动 Agent。

推荐模式：

```text
cc-connect cron
  -> bin/scheduled-check.sh
  -> ./agent-bot check --cards
  -> 需要推送时发送卡片
  -> 发送成功后记录推送状态
```

无异常时静默。异常持续时按状态机重复提醒，不允许每分钟刷屏。

## 动作安全

动作分三类：

- 只读：查看详情、重新检查、生成报告。
- 低风险：静默提醒、标记误报、记录备注。
- 高风险：重启服务、改配置、改账号状态、清理数据。

高风险动作必须：

1. 解析成预声明 `action_id`。
2. 生成预览卡片。
3. 用户确认。
4. 执行固定动作。
5. 复查验证。
6. 写审计日志。
7. 返回结果卡片。

## 密钥和配置

仓库只保存非敏感配置模板。密钥通过运行环境注入，例如：

```bash
FEISHU_APP_ID=...
FEISHU_APP_SECRET=...
```

密钥不得写入：

- Git 仓库。
- 飞书卡片。
- 按钮 payload。
- 日志。
- 测试快照。

## 测试要求

每个机器人至少覆盖：

- CLI 参数解析。
- 卡片 JSON 结构。
- 用户可见文案不泄露内部字段。
- 高风险动作确认流程。
- 定时任务静默逻辑。
- 配置缺失时的错误处理。

## 负责人视角的默认选择

- 优先构建可验证的确定性 CLI，再接 Agent。
- 优先做只读能力，再开放写操作。
- 优先做项目级权限隔离，再授权 Agent 改项目。
- 优先沉淀规范和模板，再做更复杂的平台化抽象。
