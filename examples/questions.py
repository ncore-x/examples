import logging
from typing import Callable
from functools import wraps

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def log_deco(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Вызов функции {func.__name__}")
        logging.info(f"Аргументы функции {func.__name__}: args={args}, kwargs={kwargs}")
        try:
            res = func(*args, **kwargs)
            logging.info(f"Результат функции: {res}")
            return res
        except Exception as e:
            logging.info(f"Ошибка выполнения функции {func.__name__}: {e}")
            raise
    return wrapper

@log_deco
def divide(a, b):
    return a // b

divide(10, 2)


class MyIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration


my_iter = MyIterator([1,2,3,4,5])
for ch in my_iter:
    print(ch)
