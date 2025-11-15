factorial = lambda x: 1 if x <= 1 else x * factorial(x - 1)
# recursive factorial


print(factorial(5))  # prints 120

# factorial(1) = 1
# factorial(2) = 2 * 1 = 2
# factorial(3) = 3 * 2 = 6
# factorial(4) = 4 * 6 = 24
# factorial(5) = 5 * 24 = 120
