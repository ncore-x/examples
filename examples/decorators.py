my_lambda = lambda x: x**2 if x % 2 == 0 else x
print(my_lambda(100))

# быстрое выражение
square = lambda x: x ** 2
print(square(5))

# фильтрация
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# сортировка
users = [
    {"name": "Alice", "age": 18},
    {"name": "Bob", "age": 40},
    {"name": "Alex", "age": 35},
]

sorted_users = sorted(users, key=lambda user: user["age"])
print(sorted_users)
