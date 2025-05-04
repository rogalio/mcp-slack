from functools import wraps
from typing import TypeVar, Callable, Any, Tuple, Union, Optional

T = TypeVar('T')
Result = Tuple[bool, Union[T, str]]

def api_call_handler(client_getter: Callable):
    """Decorate API calls with error handling.

    Args:
        client_getter: Function to get the API client
    """
    def decorator(func: Callable[..., T]) -> Callable[..., Result[T]]:
        @wraps(func)
        def wrapper(self, *args, **kwargs) -> Result[T]:
            try:
                # Ensure client is available
                client_getter(self)
                # Execute function and return success
                return True, func(self, *args, **kwargs)
            except Exception as e:
                # Return failure with error message
                return False, str(e)
        return wrapper
    return decorator