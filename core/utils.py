from typing import Any, Dict, Optional, Union

def create_mcp_response(
    success: bool,
    data: Optional[Any] = None,
    error: Optional[Union[str, Exception]] = None
) -> Dict[str, Any]:
    """
    Creates a standardized response dictionary for MCP tools.

    Args:
        success: Boolean indicating if the operation was successful.
        data: The result data if successful.
        error: The error message or Exception if unsuccessful.

    Returns:
        A dictionary structured for MCP tool responses.
    """
    if success:
        return {
            "success": True,
            "result": data,
            "error": None
        }
    else:
        return {
            "success": False,
            "result": None,
            "error": str(error) if error else "An unknown error occurred."
        }
