class A:
    def hello(self):
        return "Hello from A"


class B(A):
    def hello(self):
        return "Hello from B"


class C(A):
    def hello(self):
        return "Hello from C"


class D(B, C):
    pass


d = D()
print(d.hello())  # Какой метод вызовется?
print(D.mro())  # Проверяем порядок разрешения методов?

# output:
# Hello from B
# [ < class '__main__.D' > , < class '__main__.B' > , < class '__main__.C' > , < class '__main__.A' > , < class 'object' > ]

class A:
    def hello(self):
        return "Hello from A"


class B(A):
    def hello(self):
        return super().hello() + " and B"


class C(A):
    def hello(self):
        return super().hello() + " and C"


class D(B, C):
    def hello(self):
        return super().hello() + " and D"


d = D()
print(d.hello())

# output:
# Hello from A and C and B and D
