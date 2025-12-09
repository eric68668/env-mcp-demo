#!/bin/bash

# env_start.sh - Environment startup script for env-mcp-demo

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "Error: uv is not installed"
    exit 1
fi

# Install dependencies
cd "$SCRIPT_DIR/hello_world_server"
uv sync > /dev/null 2>&1

cd "$SCRIPT_DIR/calculator_server"
uv sync > /dev/null 2>&1

# Start servers
mkdir -p "$SCRIPT_DIR/logs"

# Start hello_world_server
cd "$SCRIPT_DIR/hello_world_server"
PORT=8081 nohup uv run python src/main.py > "$SCRIPT_DIR/logs/hello_world_server.log" 2>&1 &
HELLO_PID=$!
echo $HELLO_PID > "$SCRIPT_DIR/logs/hello_world_server.pid"
sleep 1

# Start calculator_server
cd "$SCRIPT_DIR/calculator_server"
PORT=8082 nohup uv run python src/main.py > "$SCRIPT_DIR/logs/calculator_server.log" 2>&1 &
CALC_PID=$!
echo $CALC_PID > "$SCRIPT_DIR/logs/calculator_server.pid"
sleep 1

# Check if servers started successfully
if ps -p $HELLO_PID > /dev/null 2>&1 && ps -p $CALC_PID > /dev/null 2>&1; then
    echo "✓ hello-world-server started (port 8081)"
    echo "✓ calculator-server started (port 8082)"
else
    echo "✗ Failed to start servers. Check logs in logs/ directory"
    exit 1
fi
