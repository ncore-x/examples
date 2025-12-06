from contextlib import contextmanager
import time
from typing import Callable
from functools import wraps
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(level)s - %(message)s"
)

# log


def messages_deco(message: str):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            logging.info(f"[LOG] {message}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# timeit


def timeit_deco(unit="seconds"):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            end = time.time()
            time_stant = end - start
            if unit == "milliseconds":
                time_stant *= 1000
            logging.info(
                f"Результат выполнения функции {func.__name__} заняло {time_stant:.4f} {unit}")
            return res
        return wrapper
    return decorator

# retry


def retry(attempts=3, delay=2):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    print(f"Attempt {attempt} failed: {e}, try again {delay}s")
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator
# cache


def cache_results(max_size: int = 128):
    def decorator(func: Callable):
        cache = {}
        order = []

        @wraps(func)
        def wrapper(*args):
            if args in cache:
                print(f"Возвращаю значение из кеша {args}")
                return cache[args]

            result = func(*args)

            if len(order) >= max_size:
                oldest = order.pop(0)
                del cache[oldest]

            cache[args] = result
            order.append(args)

            return result
        return wrapper
    return decorator


@messages_deco("ВЫВОД РЕЗУЛЬТАТА ДЕЛЕНИЯ")
@cache_results(max_size=5)
@retry(attempts=3, delay=2)
@timeit_deco(unit="milliseconds")
def divide(a, b):
    if a == 0 or b == 0:
        raise ZeroDivisionError
    result = a // b
    print(result)
    return result


print(divide(10, 2))  # вычисляется, печатается
print(divide(10, 2))  # берется из кэша, должно печатать "Возвращаем из кэша"
print(divide(4, 2))  # вычисляется
print(divide(10, 2))  # снова берется из кэша


# classmethod & staticmethod


class Human:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name: str, year: int):
        age = 2025 - year
        return cls(name, age)

    @staticmethod
    def is_adult(age: int):
        return age >= 18


u1 = Human.from_birth_year("Alex", 1990)
print(u1.name, u1.age)
print(u1.is_adult(20))


# Композиция - концепция ООП, в которой класс использует функционал другого класса без наследования


class Engine:
    def start(self):
        print("Engine started")


class Car:
    def __init__(self) -> None:
        self.engine = Engine()

    def drive(self):
        print("Car in moving")
        self.engine.start()


# mixin - класс помощник, добавляется в цепочку наследования,  добавляет новую функциональность в класс не меняя иерархии


class BaseProduct:
    pass


class CacheMixin:
    pass


class Product(CacheMixin, BaseProduct):
    pass


# __slots__ — это специальный механизм в Python, который ограничивает список допустимых атрибутов объекта и уменьшает потребление памяти.
# После объявления python больше не создает __dict__ объекту, разрешет использовать только заранее прописанные в slots атрибуты.


class Person():
    # избавляется от __dict__, тем самым ускоряя создание создание объектов и доступ к локальным свойствам класса
    __slots__ = ("name", "age")

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age


# super - функция даёт доступ к методам родительского класса, используется для расширения функционала ранее созданных классо


class Parent:
    def __init__(self, name):
        self.name = name


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age


class A:
    pass


class B(A):
    def __init__(self):
        super(B, self).__init__()  # одинаковы
        super()                   # одинаковы


# public, protected, private


class User:
    def __init__(self):
        self.__name = "John"


john = User()
print(john._User__name)  # John


# getter, setter, deleter


class Alphabet:
    def __init__(self, value) -> None:
        self._value = value

    @property  # создает из метода свойство, которое будет использоваться в setter, getter, deleter
    def value(self):
        print("Getting value")
        return self._value

    @value.setter
    def set_value(self, value):
        print("Setting value to" + str(value))
        self._value = value

    @value.deleter
    def del_value(self):
        print("Delete value")
        del self._value


alphabet = Alphabet("Hello!")
print(alphabet.value)


# contextmanager

@contextmanager
def open_file(path, mode):
    print("Открытие файла")
    f = open(path, mode)
    try:
        yield f
    finally:
        print("Закрытие файла")
        f.close()


with open_file("text.txt", "w") as f:
    f.write("Hello")


@contextmanager
def timer():
    start = time.time()
    yield
    end = time.time()
    time_difference = end - start
    print(f"Время выполнения:, {time_difference:.3f}")


with timer():
    sum(range(10_000_000))


# metaclass
# Метаклассы - шаблон для классов. Основная цель метаклассов - автоматически изменять класс в момент создания.

class MyMeta(type):
    def __new__(cls, name, bases, dct):
        # изменения в классе
        dct["new_method"] = lambda self: print("New method added!")
        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=MyMeta):
    def existing_method(self):
        print("Existing method.")


obj = MyClass()
obj.new_method()  # New method added!
obj.existing_method()  # Existing method.

# класс без class
# С помощью функции type. Помимо того, что эта функция возвращает класс, к которому принадлежит переданный в нее инстанс, она также является встроенным метаклассом и  может быть использована для создания классов.
# Она принимает три аргумента: name: str - имя класса; bases: tuple - передаваемые классы, наследование; dict: dict - словарь с атрибутами, ключ - имя метода, значение - сами атрибуты
User = type("User", (), {})
