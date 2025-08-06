#!/usr/bin/env bash

# anchor_restore_gate.sh v3
# This hook guides the agent to the Anchor Restore Protocol.

set -euo pipefail

# Get project root relative to this script's location
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
LOCK_FILE="$PROJECT_ROOT/.anchor/protected/anchor.lock"
RESTORE_INSTRUCTIONS_PATH="$PROJECT_ROOT/.anchor/accessible/anchor_restore.md"

# If no lock file exists, allow all operations
if [ ! -f "$LOCK_FILE" ]; then
  exit 0
fi

# System is paused. Read JSON input from stdin to check the command.
input=$(cat)
command_text=""

# Use jq if available for robust command extraction
if command -v jq >/dev/null 2>&1; then
  command_text=$(echo "$input" | jq -r '.tool_input.command // empty' 2>/dev/null)
fi

# Allow access to the '.anchor/accessible/' directory for restore.
# This check covers both jq-parsed commands and raw input as a fallback.
if [[ "$command_text" == *".anchor/accessible/"* ]] || [[ "$input" == *".anchor/accessible/"* ]]; then
  exit 0
fi

# Allow subagent operations under main agent authority.
# Subagents are tools of the validated main agent, not independent agents requiring restoration.
if [[ "$input" == *"subagent_type"* ]] || [[ "$command_text" == *"subagent_type"* ]]; then
  exit 0
fi

# Block everything else with a clear, helpful, and actionable message.
# This is not an error, but a guided instruction.
echo "
🛑 COGNITIVE CHECKPOINT ACTIVATED

Your context may be compromised. For your protection:

1. STOP ALL WORK IMMEDIATELY
2. Save any active files to: .anchor/tmp/[filename]
3. DO NOT continue any tasks until restoration complete
4. Follow protocol: cat \"$RESTORE_INSTRUCTIONS_PATH\"

This protects your work quality and prevents context drift.
" >&2
exit 2