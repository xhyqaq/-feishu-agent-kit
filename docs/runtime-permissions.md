# 运行权限模型

`work_dir`、`AGENTS.md` 和提示词不能作为安全边界。生产环境必须有操作系统或容器级隔离。

## 推荐边界

- 每个机器人一个独立项目目录。
- 每个机器人一个独立低权限宿主用户。
- 每个机器人一份最小 cc-connect 配置副本。
- Agent 容器只挂载当前项目目录为可写。
- 全局 cc-connect 配置、secret、SSH key、其他项目目录不向 Agent 可写开放。

## 不推荐做法

- 让 root 直接执行项目目录里可被 Agent 修改的脚本。
- 把低权限用户加入 `docker` 组。
- 把全局 `/opt/cc-connect/config.toml` 挂进 Agent 容器。
- 把多个机器人共用同一份可写 HOME。
- 依赖提示词阻止 Agent 写其他目录。

## 推荐执行链路

```text
cc-connect.service
  -> root-owned launcher
  -> setpriv / sudo -u bot-user
  -> project bin/*.sh
  -> project CLI
```

Agent 自然语言链路：

```text
cc-connect
  -> codex wrapper
  -> Docker container user 10001:10001
  -> mount current project as rw
  -> mount project Codex home as rw
  -> mount minimal config as ro
```

## 验收条件

上线前必须验证：

- 低权限宿主用户能写本项目。
- 低权限宿主用户不能写其他项目。
- Agent 容器能写本项目。
- Agent 容器不能看到全局配置。
- 定时任务正常执行。
- 无异常时定时任务静默。
- 飞书用户不会看到 shell 成功但无输出这类噪音。
