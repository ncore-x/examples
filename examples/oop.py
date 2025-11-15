name = "Tom"  # immutable data type
cat = {"name": "Tom", "age": 3}


def change_name(name):
    name = "Jerry"  # local variable
    return name


def change_cat(a_dict):
    a_dict.clear()  # {"name": "Tom", "age": 3}
    a_dict = {"name": "Jerry", "age": 5}  # local variable
    # a_dict.update({'name': 'Jerry', 'age': 3})
    return a_dict  # will be removed by the garbage collector, since it is not assigned anywhere


change_name(name)  # name = change_name(name), res = "Jerry"
change_cat(cat)  # cat = change_cat(cat), res = {"name": "Jerry", "age": 5}

print(name)  # Tom
print(cat)  # {}
