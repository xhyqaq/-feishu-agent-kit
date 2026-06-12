#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <bot-name> <target-dir>" >&2
  exit 64
fi

bot_name="$1"
target_dir="$2"

case "$bot_name" in
  ""|*[!a-zA-Z0-9_-]*)
    echo "bot-name must contain only letters, numbers, _ or -" >&2
    exit 64
    ;;
esac

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
repo_root="$(cd "$script_dir/.." && pwd -P)"
template_dir="$repo_root/template"

if [[ -e "$target_dir" ]]; then
  echo "target-dir already exists: $target_dir" >&2
  exit 73
fi

mkdir -p "$target_dir"

copy_one() {
  local src="$1"
  local dst="$2"
  if [[ -d "$src" ]]; then
    mkdir -p "$dst"
    return
  fi
  mkdir -p "$(dirname "$dst")"
  sed "s/{{BOT_NAME}}/$bot_name/g" "$src" > "$dst"
}

while IFS= read -r rel; do
  rel="${rel#./}"
  copy_one "$template_dir/$rel" "$target_dir/$rel"
done < <(cd "$template_dir" && find . -name .DS_Store -prune -o -type f -print | sort)

chmod +x "$target_dir/agent-bot" "$target_dir"/bin/*.sh

cat > "$target_dir/.gitignore" <<'GITIGNORE'
__pycache__/
*.pyc
.DS_Store
logs/
state/
*.env
GITIGNORE

echo "Created $bot_name at $target_dir"
