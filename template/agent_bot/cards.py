from __future__ import annotations


def result_card(title: str, summary: str) -> dict:
    return {
        "schema": "2.0",
        "config": {"update_multi": True},
        "header": {"title": {"tag": "plain_text", "content": title}, "template": "blue"},
        "body": {
            "direction": "vertical",
            "padding": "12px 12px 12px 12px",
            "elements": [{"tag": "markdown", "content": summary}],
        },
    }
