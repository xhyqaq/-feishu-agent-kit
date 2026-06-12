#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/runtime-env.sh"

log_dir="logs"
mkdir -p "$log_dir"

./agent-bot check --json --title "{{BOT_NAME}} 定时检查" > "$log_dir/scheduled-check.json"
