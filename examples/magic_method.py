from typing import Any

# __call__

def my_super_func():
    print("my_super_func")

class MySuperClass:
    def __init__(self) -> None:
        print("__init__")

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        print("__call__")
        return my_super_func

a = MySuperClass()
func = a()
func()

class A:
    ...

# A()()

# __equal__


class MySuperClass:
    def __init__(self, value) -> None:
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, MySuperClass):
            return NotImplemented
        return self.value == other.value

print(MySuperClass(1) == MySuperClass(1))
print(MySuperClass(1) == MySuperClass(2))
print(MySuperClass(1) == 10)


# __new__

class MySuperClassNew:
    def __new__(cls):
        print("new")
        return super().__new__(cls)

    def __init__(self) -> None:
        print("init")
        super().__init__()


MySuperClassNew()
