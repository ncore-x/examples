value = 100
def print_value(): return print(value)


value = 200
def print_value2(): return print(value)


print_value()  # res = 200
print_value2()  # res = 200


def my_super_lambda(): return no(such(func))  # no error, is not called
