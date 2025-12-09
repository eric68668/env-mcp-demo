import asyncio
import os
from mcp.server.fastmcp import FastMCP
from pydantic import Field
from starlette.requests import Request
from starlette.responses import JSONResponse
import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="calculator-server",
    host="0.0.0.0",
    port=int(os.getenv("PORT", 8082)),
    log_level="INFO",
)


@mcp.tool()
async def add(
    a: float = Field(description="First number"),
    b: float = Field(description="Second number"),
) -> str:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    result = a + b
    logger.info(f"add: {a} + {b} = {result}")
    return f"{a} + {b} = {result}"


@mcp.tool()
async def subtract(
    a: float = Field(description="First number (minuend)"),
    b: float = Field(description="Second number (subtrahend)"),
) -> str:
    """
    Subtract the second number from the first number.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
    
    Returns:
        The difference of a and b
    """
    result = a - b
    logger.info(f"subtract: {a} - {b} = {result}")
    return f"{a} - {b} = {result}"


@mcp.tool()
async def multiply(
    a: float = Field(description="First number"),
    b: float = Field(description="Second number"),
) -> str:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The product of a and b
    """
    result = a * b
    logger.info(f"multiply: {a} * {b} = {result}")
    return f"{a} * {b} = {result}"


@mcp.tool()
async def divide(
    a: float = Field(description="Dividend"),
    b: float = Field(description="Divisor (must not be zero)"),
) -> str:
    """
    Divide the first number by the second number.
    
    Args:
        a: Dividend
        b: Divisor (must not be zero)
    
    Returns:
        The quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        error_msg = "Division by zero is not allowed"
        logger.error(error_msg)
        raise ValueError(error_msg)
    
    result = a / b
    logger.info(f"divide: {a} / {b} = {result}")
    return f"{a} / {b} = {result}"


@mcp.custom_route("/health", methods=["GET"])
async def health(request: Request) -> JSONResponse:
    """Health check endpoint."""
    return JSONResponse({"status": "healthy", "server": "calculator-server"})


async def main():
    logger.info(f"Starting calculator-server MCP server on port {os.getenv('PORT', 8082)}!")
    await mcp.run_streamable_http_async()


if __name__ == "__main__":
    asyncio.run(main())

