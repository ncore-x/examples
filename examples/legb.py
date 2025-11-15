value = 100


def outer_function():
    def inner_function():
        print(len(my_list))  # res = 0
        print(len(value))  # res = 0

    my_list = [1, 2, 3]
    def length(x): return 0
    len = length  # override built-in function len

    inner_function()


outer_function()
