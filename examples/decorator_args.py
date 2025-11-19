from functools import wraps


def typed(*types):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i, arg in enumerate(args):
                if not isinstance(arg, types):
                    raise ValueError(
                        f"arg #{i} ({arg!r}) must be instance of {types}")
            for name, val in kwargs.items():
                if not isinstance(val, types):
                    raise ValueError(
                        f"kwarg '{name}' ({val!r}) must be instance of {types}")
            return func(*args, **kwargs)
        return wrapper
    return decorator


@typed(str)
def convert(a, b):
    return a + b


@typed(int)
def calculate(a, b, c):
    return a + b * c


print(convert('Д', 'а'))
print(calculate(2, 2, 2))
