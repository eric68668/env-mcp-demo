# env-mcp-demo

Dynamic MCP Server Demo with Hello World and Calculator servers.

## Project Structure

```
env-mcp-demo/
├── hello_world_server/      # Hello World MCP Server
│   ├── src/
│   │   └── main.py         # Server implementation
│   └── pyproject.toml      # uv project config
├── calculator_server/       # Calculator MCP Server
│   ├── src/
│   │   └── main.py         # Server implementation
│   └── pyproject.toml      # uv project config
├── mcp_config.py           # MCP servers configuration
├── env_start.sh            # Environment setup script
├── metadata.json           # Project metadata
├── pyproject.toml          # Root project config
└── README.md               # This file
```

## MCP Servers

### Hello World Server

A simple MCP server that provides a single tool:
- `hello_world`: Outputs "Hello World!"

### Calculator Server

A calculator MCP server with four arithmetic operations:
- `add`: Add two numbers
- `subtract`: Subtract two numbers
- `multiply`: Multiply two numbers
- `divide`: Divide two numbers

## Setup

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Run the setup script:
   ```bash
   chmod +x env_start.sh
   ./env_start.sh
   ```

## Usage

### Start Hello World Server (Streamable HTTP)

```bash
cd hello_world_server
PORT=8081 uv run -m main
```

The server will start on `http://localhost:8081`. You can check health at `http://localhost:8081/health`.

### Start Calculator Server (Streamable HTTP)

```bash
cd calculator_server
PORT=8082 uv run -m main
```

The server will start on `http://localhost:8082`. You can check health at `http://localhost:8082/health`.

### MCP Endpoints

- Hello World Server: `http://localhost:8081/mcp`
- Calculator Server: `http://localhost:8082/mcp`

### Configuration

The `mcp_config.py` file is configured to use `streamable_http` mode. You can override the server URLs using environment variables:

```bash
export HELLO_WORLD_SERVER_URL=http://localhost:8081
export CALCULATOR_SERVER_URL=http://localhost:8082
```

## Configuration

The `mcp_config.py` file contains the configuration for both MCP servers. It defines how the servers are started and their runtime parameters.

## Metadata

The `metadata.json` file contains project metadata including:
- Server information
- Available tools
- Dependencies
- Configuration files

