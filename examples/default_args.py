def func(array = None):
    if array is None:
        array = []
    array.append(4)
    return array

print(func([1,2,3]))
