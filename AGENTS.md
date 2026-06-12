- 必须用中文回复。
- 这个目录是 `feishu-agent-kit` 的模板仓库工作目录，不是任何具体飞书机器人的运行目录。
- 本仓库用于沉淀飞书 Agent 机器人的技术规范、项目模板和脚手架。
- `template/AGENTS.md` 是生成新机器人项目时复制出去的开发目录规则；当前仓库自身的规则以本文件为准。
- `template/feishu-runtime/AGENTS.md` 是生成项目里的飞书运行态规则模板；不要把它当成本仓库的运行规则。

## 工作边界

- 修改模板时，要区分“模板仓库自身文件”和“生成项目产物文件”。
- 需要让 Codex、Claude Code 等 Agent 在本仓库工作时读取的规则，放在仓库根目录。
- 需要让生成出来的新机器人项目读取的规则，放在 `template/` 下。
- 涉及飞书消息格式、Card JSON、按钮回调、cc-connect 配置或 Agent 运行方式时，先读取 `docs/official-references.md` 并按官方文档核对，不要只凭记忆写。
- 不要把某个业务机器人的专有 IP、密钥、账号、服务名写进通用模板。
- 可以在文档里说明模板来源于已上线实践，但模板主体应保持业务无关。

## 模板约束

- `scripts/create-bot.sh` 生成的新项目必须包含根目录 `AGENTS.md` 和 `feishu-runtime/AGENTS.md`。
- 生成项目后，根目录 `AGENTS.md` 服务于开发/维护工作目录。
- 生成项目后，`feishu-runtime/AGENTS.md` 服务于飞书 Agent 的运行态工作目录。
- 新增模板文件后，要确认 `{{BOT_NAME}}` 占位符能被脚手架替换。

## 验证

修改模板、脚手架或 README 后运行：

```bash
python3 -m unittest discover -s tests -v
```

如果修改 `scripts/create-bot.sh`，还要确认生成项目中没有残留 `{{BOT_NAME}}`。

## 用户可见内容要求

- README 和 docs 面向开发者、维护者，不写成飞书终端用户文案。
- `template/feishu-runtime/AGENTS.md` 面向未来生成项目的飞书运行态，不应暴露开发过程、测试过程、内部实现细节或密钥路径。
