from functools import wraps
import time
from typing import Callable

# log


def logger(message: str) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


def async_logger(message: str) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            print(f"[LOG] {message}")
            return await func(*args, **kwargs)
        return wrapper
    return decorator

# time


def timeit(unit: str = "seconds") -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            elapsed = end - start
            if unit == "milliseconds":
                elapsed *= 1000
            print(f"[TIME] {func.__name__} executed in {elapsed:.5f} {unit}")
            return result
        return wrapper
    return decorator


def async_timeit(unit: str = "seconds") -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = await func(*args, **kwargs)
            end = time.perf_counter()
            elapsed = end - start
            if unit == "milliseconds":
                elapsed *= 1000
            print(f"[TIME] {func.__name__} executed in {elapsed:.5f} {unit}")
            return result
        return wrapper
    return decorator

# retry


def retry(attempts: int = 3, delay: int = 2) -> Callable:
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(
                        f" [RETRY] Attempt {attempt} failed: {e} try again in {delay} seconds...")
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator


# cache
def cache(max_size: int = 128) -> Callable:
    def decorator(func: Callable):
        cache = {}
        order = []

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                return cache[args]

            result = func(*args)
            print(f"[CACHE] Caching result for args: {args}")

            cache[args] = result
            order.append(args)

            if len(cache) >= max_size:
                oldest = order.pop(0)
                del cache[oldest]

            return result
        return wrapper
    return decorator


@cache()
@retry()
@timeit("milliseconds")
@logger("Деление двух чисел")
def divide(a, b):
    if a == 0 or b == 0:
        raise ValueError("Деление на ноль недопустимо")
    return f"Результат: {a // b}"


print(divide(10, 2))
print(divide(10, 2))
print(divide(10, 5))
print(divide(10, 2))
print(divide(10, 2))
