from typing import TypedDict, Optional, Any

class ToolResult(TypedDict):
    """Standard return type for all MCP tools."""
    success: bool
    result: Optional[Any]
    error: Optional[str]
