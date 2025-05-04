from typing import TypeVar, Callable, Any, Dict, Union, List, Optional
from functools import wraps
from core.decorators import api_call_handler

T = TypeVar('T')
E = TypeVar('E', bound=Union[str, Dict, List])


def tool_response(success: bool, data: Any = None, error: Optional[Any] = None) -> Dict[str, Any]:
    """Create standardized tool response."""
    return {
        "success": success,
        "result": data if success else None,
        "error": str(error) if error and not success else None
    }

def resource_response(success: bool, data: Any) -> Any:
    """Handle resource response consistently."""
    return data if success else str(data)

