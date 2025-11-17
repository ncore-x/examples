class MyList(list):
    def __str__(self):
        return super().__str__().replace(',', ',\n')


my_list = MyList([1, 2, 3, 4, 5])
print(my_list)

# Output: [1,
#          2,
#          3,
#          4,
#          5]


class A:
    def process(self):
        return "A start\nA end\n"


class B(A):
    def process(self):
        s = "B start\n"
        s += super().process()
        s += "B end\n"
        return s


class C(A):
    def process(self):
        s = "C start\n"
        s += super().process()
        s += "C end\n"
        return s


class D(C, B):
    pass


d = D()
print(d.process())

# Output:
# C start
# B start
# A start
# A end
# B end
# C end

# super — это встроенная функция, которая возвращает прокси-объект, позволяющий вызвать метод родительского класса в контексте текущего экземпляра. Основные применения:
# вызвать реализацию метода в базовом классе(например, init, save, str),
# расширить поведение родителя(выполнить родительскую логику, затем добавить своё),
# обеспечить корректную работу при множественном наследовании за счёт единой цепочки вызовов по MRO(cooperative multiple inheritance).
