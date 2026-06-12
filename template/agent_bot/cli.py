from __future__ import annotations

import argparse
import json
from pathlib import Path

from .cards import result_card


def print_json(value: object) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def command_check(args: argparse.Namespace) -> int:
    card = result_card(args.title, "**整体状态**：正常\n**检查结果**：模板检查已完成。")
    if args.json:
        print_json(card)
    else:
        print("检查完成")
    return 0


def command_send_card(args: argparse.Namespace) -> int:
    card = json.loads(Path(args.card_file).read_text(encoding="utf-8"))
    if not args.yes:
        print_json({"dry_run": True, "card": card})
        return 0
    # 新项目应在这里接入飞书发送逻辑，或复用已有内部发送器。
    print_json({"sent": True})
    return 0


def command_action(args: argparse.Namespace) -> int:
    card = result_card("操作结果", f"已收到动作请求：`{args.payload}`")
    print_json(card)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-bot")
    sub = parser.add_subparsers(dest="command", required=True)

    check = sub.add_parser("check", help="Run a deterministic check")
    check.add_argument("--json", action="store_true")
    check.add_argument("--title", default="{{BOT_NAME}} 检查")
    check.set_defaults(func=command_check)

    send = sub.add_parser("send-card", help="Send or dry-run a card")
    send.add_argument("--card-file", required=True)
    send.add_argument("--yes", action="store_true")
    send.set_defaults(func=command_send_card)

    action = sub.add_parser("action", help="Handle a card action")
    action.add_argument("--payload", required=True)
    action.set_defaults(func=command_action)

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
