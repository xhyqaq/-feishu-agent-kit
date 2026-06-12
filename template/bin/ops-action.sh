#!/usr/bin/env bash
set -euo pipefail
source "$(dirname "$0")/runtime-env.sh"

payload="${1:-}"
./agent-bot action --payload "$payload"
