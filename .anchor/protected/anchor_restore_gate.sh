#!/bin/bash

# anchor_restore_gate.sh
# This hook enforces the Anchor Checkpoint System.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOCK_FILE="$PROJECT_ROOT/.anchor/protected/anchor.lock"

# If no lock file exists, allow all operations
if [ ! -f "$LOCK_FILE" ]; then
  exit 0
fi

# System is paused - read JSON input from stdin
input=$(cat)

# Use jq to extract the command from tool_input (if available)
if command -v jq >/dev/null 2>&1; then
  command_text=$(echo "$input" | jq -r '.tool_input.command // empty' 2>/dev/null)
  
  # Only allow .anchor/accessible/ access
  if [[ "$command_text" == *".anchor/accessible/"* ]]; then
    exit 0
  fi
fi

# Fallback: check raw input for accessible path
if [[ "$input" == *".anchor/accessible/"* ]]; then
  exit 0
fi

# Block everything else with clear message
echo "🔒 Anchor Checkpoint System ACTIVE" >&2
echo "Only '.anchor/accessible/' tools and files are permitted." >&2
echo "Run '.anchor/accessible/bin/anchor-restore' to begin restore process." >&2
exit 2