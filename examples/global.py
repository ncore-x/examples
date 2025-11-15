global value  # ДОЛЖЕН ИСПОЛЬЗОВАТЬСЯ ВНУТРИ ФУНКЦИИ
value = 100


def print_value():
    print(value)


def change_value():
    # global value  # РАСКОММЕНТИРУЙТЕ ЭТУ СТРОКУ, ЧТОБЫ ИСПРАВИТЬ ОШИБКУ
    value += 100
    print(value)


print_value()
change_value()
print_value()
# UnboundLocalError: local variable 'value' referenced before assignment
