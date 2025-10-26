import random
import time
from functools import wraps
from typing import Any, Callable, TypeVar, cast

F = TypeVar('F', bound=Callable[..., Any])

def retry(tries: int, delay: float) -> Callable[[F], F]:
    """Retry decorator
    usage:
    @retry(tries=3, delay=0.2)
    def my_function():
        ...
    """
    def decorator(fn: F) -> F:
        @wraps(fn)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            for attempt in range(tries):
                result = fn(*args, **kwargs)
                if result is not None:
                    return result
                time.sleep(delay)
            return fn(*args, **kwargs)
        return cast(F, wrapper)
    return decorator


@retry(tries=10, delay=0.5)
def fetch_data() -> str | None:
    """Simulate an unreliable call returning None on failure"""
    print("Trying to fetch...")
    return "Success!" if random.random() > 0.7 else None

if __name__ == "__main__":
    print(fetch_data())
