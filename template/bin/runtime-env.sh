#!/usr/bin/env bash

export PATH="/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:${PATH:-}"

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
project_root="$(cd "$script_dir/.." && pwd -P)"
cd "$project_root"

export BOT_PROJECT_ROOT="${BOT_PROJECT_ROOT:-$project_root}"
export CC_CONNECT_CONFIG="${CC_CONNECT_CONFIG:-}"
if [[ -z "$CC_CONNECT_CONFIG" ]]; then
  if [[ -f "/opt/cc-connect/{{BOT_NAME}}/config.toml" ]]; then
    export CC_CONNECT_CONFIG="/opt/cc-connect/{{BOT_NAME}}/config.toml"
  elif [[ -f /opt/cc-connect/config.toml ]]; then
    export CC_CONNECT_CONFIG="/opt/cc-connect/config.toml"
  else
    export CC_CONNECT_CONFIG="$HOME/.cc-connect/config.toml"
  fi
fi

if [[ -f "$HOME/.config/{{BOT_NAME}}/env" ]]; then
  set -a
  # shellcheck disable=SC1090
  source "$HOME/.config/{{BOT_NAME}}/env"
  set +a
fi
