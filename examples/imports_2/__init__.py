import foo

# from foo.bar.baz import BAZ  # prints 3
# from foo.bar import BAR  # prints 2
# from foo import FOO  # prints 1

print(foo.bar)  # prints the foo.bar module
print(foo.bar.baz)  # prints the foo.bar.baz module
print(foo.bar.baz.BAZ)  # prints 3
print(foo.bar.BAR)  # prints 2
# print(FOO + BAR + BAZ)  # ERROR: FOO, BAR, and BAZ are not defined in this scope
print(foo.FOO + foo.bar.BAR + foo.bar.baz.BAZ)  # prints 6
