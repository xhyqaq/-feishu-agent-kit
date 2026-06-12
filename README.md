# Feishu Agent Kit

用于创建和治理飞书 Agent 机器人的项目模板。

这个仓库沉淀自一个已经上线运行的飞书运维机器人实践，但这里不绑定具体业务。它提供三类产物：

- 技术规范：定义飞书 Agent 机器人的架构、安全边界、交互方式和工程约束。
- 项目模板：定义一个新机器人项目应具备的目录结构、运行入口、规则文件和测试骨架。
- 脚手架：用一条命令复制模板，快速生成新的机器人项目。

## 适用场景

适合用来创建这类机器人：

- 运维巡检机器人
- 内部工具机器人
- 业务状态查询机器人
- 带飞书卡片交互的 Agent
- 需要自然语言理解，但写操作必须受控的自动化机器人

不适合直接用于：

- 纯闲聊机器人
- 没有权限边界要求的一次性脚本
- 只需要一个 Webhook 的简单通知机器人

## 核心架构

```text
Feishu 用户
  |
  v
cc-connect
  |
  +-- commands / cron -> bin/*.sh -> project CLI
  |
  +-- natural language -> Codex Agent -> feishu-runtime work_dir
  |
  v
机器人项目
  - agent_bot: 确定性工具层
  - bin: cc-connect 命令和定时任务入口
  - feishu-runtime: 飞书运行态规则
  - config: 非敏感配置模板
  - docs: 架构、部署、权限文档
  - tests: 回归测试
```

核心边界是：确定性逻辑进入 CLI 和 shell wrapper，自然语言理解交给 Agent，高风险写操作必须经过确认、执行、验证和审计。

## 依赖项目和运行时

这个仓库本身只提供规范、模板和脚手架，不内置飞书网关、Agent CLI 或生产隔离环境。使用时需要配合以下组件。

**必需依赖**

- 飞书开放平台机器人：提供消息入口、卡片消息、按钮回调和应用凭据。
- cc-connect：连接飞书和本地/服务器 Agent，负责 project、command、cron、card callback 等桥接能力。
- Codex 或 Claude Code：作为自然语言 Agent，处理用户开放请求、复杂排查和代码修改。
- Python 3.11+：模板内置 CLI 和测试骨架使用 Python 标准库实现。
- Git：用于管理生成后的机器人项目。

**生产部署依赖**

- Linux/systemd：推荐用 systemd 管理 cc-connect 或项目相关服务。
- Docker：当 Agent 需要容器化隔离时使用，例如让 Codex 只挂载当前项目目录。
- OS 权限工具：例如 `setpriv`、专用低权限用户、文件属主和 ACL，用于实现硬权限边界。
- secret 管理方式：例如 systemd `EnvironmentFile`、独立 secret 文件或平台密钥管理，不要把密钥写进 Git。

**可选依赖**

- 业务 API 或内部系统 SDK：由具体机器人决定，例如监控系统、账号系统、审批系统、知识库系统。
- 飞书 OpenAPI 封装工具：如果机器人需要主动查询或操作更多飞书资源，可以在生成项目后接入。
- 额外 Agent skills：如果某类业务有稳定 API，可以沉淀成 skill 供 Agent 使用。

依赖关系可以理解为：

```text
feishu-agent-kit
  -> 生成机器人项目骨架
  -> 接入 cc-connect
  -> cc-connect 接入飞书和 Agent CLI
  -> 机器人项目按需接入业务 API / 内部系统
```

## 快速开始

生成一个新机器人项目：

```bash
cd /Users/xhy/Project/feishu-agent-kit
./scripts/create-bot.sh my-agent-bot /Users/xhy/Project/my-agent-bot
```

验证生成结果：

```bash
cd /Users/xhy/Project/my-agent-bot
python3 -m unittest discover -s tests -v
```

生成后的项目会包含：

```text
my-agent-bot/
  AGENTS.md
  README.md
  agent-bot
  agent_bot/
  bin/
  config/
  docs/
  feishu-runtime/
  tests/
```

## 仓库结构

```text
feishu-agent-kit/
  AGENTS.md
  CLAUDE.md
  README.md
  docs/
    official-references.md
    technical-standard.md
    project-template.md
    runtime-permissions.md
  scripts/
    create-bot.sh
  template/
    AGENTS.md
    CLAUDE.md
    feishu-runtime/AGENTS.md
    feishu-runtime/CLAUDE.md
    agent_bot/
    bin/
    config/
    docs/
    tests/
  tests/
    test_scaffold.py
```

这里有两个层级的 `AGENTS.md`，用途不同：

- `AGENTS.md`：当前模板仓库自己的工作目录规则，Codex、Claude Code 等 Agent 在维护这个仓库时读取。
- `template/AGENTS.md`：生成新机器人项目时复制到新项目根目录的规则文件。
- `template/feishu-runtime/AGENTS.md`：生成新机器人项目时复制到运行态目录的规则文件，供飞书 Agent 的 `work_dir` 使用。

`CLAUDE.md` 只做一件事：引用同目录的 `AGENTS.md`。这样 Claude Code 和 Codex 能共享同一份规则入口，避免两套规范漂移。

## 三层产物

**官方规范索引**

[docs/official-references.md](docs/official-references.md) 收录飞书/Lark、cc-connect、Codex 和 Claude Code 的官方文档入口。开发消息格式、卡片 JSON、按钮回调、cc-connect 配置或 Agent 运行方式时，应先查这个索引里的官方文档，避免 AI 只凭记忆生成过时语法。

**技术规范**

[docs/technical-standard.md](docs/technical-standard.md) 定义机器人通用标准，包括：

- 飞书、cc-connect、Agent、CLI 的职责边界
- 飞书 Card JSON 2.0 交互规范
- 确定性任务和自然语言任务的分工
- 高风险动作的确认和审计链路
- 密钥、日志、按钮 payload 的安全要求
- 最低测试要求

**项目模板**

[docs/project-template.md](docs/project-template.md) 说明模板生成的新项目结构，以及每个目录和入口的职责。

模板内容位于 [template](template)，新机器人项目会从这里复制生成。

**脚手架**

[scripts/create-bot.sh](scripts/create-bot.sh) 负责把模板复制到目标目录，并替换 `{{BOT_NAME}}` 占位符。

```bash
./scripts/create-bot.sh <bot-name> <target-dir>
```

示例：

```bash
./scripts/create-bot.sh cost-agent /Users/xhy/Project/cost-agent
```

## 设计原则

- 飞书是交互层，不是命令行输出窗口。
- 用户可见结果优先使用飞书交互卡片。
- 确定性逻辑必须可本地运行、可测试、可审计。
- Agent 负责理解和推理，不负责绕过确认流程直接执行高风险动作。
- `work_dir` 和 `AGENTS.md` 只是行为约束，不是操作系统安全边界。
- 生产环境必须设计低权限用户、目录权限、容器挂载和最小配置。
- 正常定时任务应静默，只有异常、恢复、重复提醒或用户主动请求才发卡片。

## 生成项目后的改造点

生成项目只是骨架。创建新机器人后，通常需要按这个顺序改：

1. 修改 `README.md`，说明这个机器人解决什么问题。
2. 修改 `AGENTS.md`，定义开发目录规则。
3. 修改 `feishu-runtime/AGENTS.md`，定义飞书用户可见能力和边界。
4. 修改 `config/targets.example.toml`，放入非敏感配置模板。
5. 在 `agent_bot/cli.py` 中实现确定性命令。
6. 在 `agent_bot/cards.py` 中实现飞书卡片。
7. 在 `bin/*.sh` 中接入 cc-connect command 和 cron。
8. 补充测试，尤其是卡片结构和敏感信息泄露检查。
9. 设计生产运行权限边界。
10. 先上线只读能力，再开放写操作。

## cc-connect 接入示例

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

生产环境中，`exec` 推荐指向 root 拥有的降权启动器，再由启动器降权执行项目脚本，避免 root 直接执行 Agent 可写目录中的文件。

## 权限要求

生产部署前至少验证：

- 低权限宿主用户能写本机器人项目。
- 低权限宿主用户不能写其他项目。
- Agent 容器能写本机器人项目。
- Agent 容器看不到全局 cc-connect 配置。
- secret 不进入 Git、日志、卡片、按钮 payload。
- cron 正常执行，且无异常时静默。

详细说明见 [docs/runtime-permissions.md](docs/runtime-permissions.md)。

## 本仓库验证

```bash
python3 -m unittest discover -s tests -v
```

测试会实际调用脚手架生成一个临时机器人项目，并验证生成后的项目测试可通过。

## 后续演进

当前版本是最小可用模板。后续可以继续沉淀：

- cc-connect 配置生成器
- 生产部署脚本
- root-owned launcher 模板
- 飞书卡片组件库
- action contract 生成器
- secret 和权限验收脚本
