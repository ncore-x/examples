def my_gen(data):
    for item in data:
        yield item


# 1
gen = my_gen([1, 2, 3, 4, 5])

# 2
generator = (x for x in [1, 2, 3, 4])

# 3
data = [1,2,3,4,5]
[x for x in data]
next(gen)

def custom_gen():
    yield 1
    yield 2
    yield 3


gena = custom_gen()

print(next(gena)) # 1
print(next(gena)) # 2
print(next(gena)) # 3

generator = (i for i in range(5))

def number():
    while True:
        yield 1

print(next(number()))
