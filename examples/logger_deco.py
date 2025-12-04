import logging

# Настройка логирования в файл
logging.basicConfig(
    filename="app.log",           # имя файла
    level=logging.INFO,           # уровень логирования
    format="%(asctime)s — %(levelname)s — %(message)s"
)

def file_logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Вызов функции: {func.__name__}")
        logging.info(f"Аргументы: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Результат: {result}")
            return result
        except Exception as e:
            logging.error(f"Ошибка в функции {func.__name__}: {e}")
            raise
    return wrapper


@file_logger
def divide(a, b):
    return a // b


divide(10, 5)



class Decorator:
    def __init__(self, func) -> None:
        self._func = func

    def __call__(self, *args, **kwargs):
        print("before decorator")
        result = self._func(*args, **kwargs)
        print("after decorator")
        return result


@Decorator
def summator(a: int, b: int) -> int:
    print('function')
    return a + b

# summator = Decorator(summator) ~ Decorator(summator).__call__
print(summator(1, 2)) # Decorator(summator)(1, 2)


def add_some_property(original_class):
    original_init = original_class.__init__

    def __init__(self, *args, **kwargs):
        self.additional_property = 'a'
        original_init(self, *args, **kwargs)

    original_class.__init__ = __init__
    return original_class


@add_some_property
class Foo:
    pass


# вот что сделает наш интерпретатор: Foo = add_some_property(Foo)
kek = Foo()
print(f'new property: {kek.additional_property}')
