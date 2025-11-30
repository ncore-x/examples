# Итератор - это поведенческий паттерн проектирования, позволяющий совершать последовательный обход элементов составных объектов, не раскрывая их внутреннего представления

my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))  # ERROR: Stop Iteration


# Генератор — это объект, реализующий протокол итератора, при этом генератор не хранит весь итерируемый набор элементов в памяти, вместо этого производя генерацию элементов “на лету”.
# Генераторные выражения:

example1 = [x**x for x in range(10)]
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

example2 = (x**x for x in range(10))
# <generator object <genexpr> at 0x7fe76f7e5db0>
