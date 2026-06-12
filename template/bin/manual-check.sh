#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/runtime-env.sh"

./agent-bot check --json --title "{{BOT_NAME}} 检查"
