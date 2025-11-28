from functools import wraps
from typing import Callable


def log(message: str):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@log("Функция запускается!")
def hello(name: str):
    print(f"Привет, {name}!")


hello("Ашот")
