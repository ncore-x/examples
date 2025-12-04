class MyIterator:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1
            return res
        else:
            raise StopIteration


my_iter = MyIterator([1, 2, 3, 4, 5])

for item in my_iter:
    print(item)


class MyIterationObject:
    def __init__(self, data) -> None:
        self.data = data

    def __iter__(self):
        return Iterator(self.data)


class Iterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


print("#")


class SquaresIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.data):
            res = self.data[self.index]
            self.index += 1

            if isinstance(res, int):
                return res ** 2

        raise StopIteration


my_it = SquaresIterator([1, "a", 3, 4, 5])

for i in my_it:
    print(i)

print("#")
gen_expr = (x for x in range(5))
reversed_gen = reversed(list(gen_expr))
# reversed_gen =list(gen_expr)[::-1]
print(list(reversed_gen))


#filemanager

class FileManager:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, s):
        self.file.close()

    async def __aenter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    async def __aexit__(self, type, value, traceback):
        self.file.close()


with FileManager('example.txt', 'w') as file:
    file.write("Привет, это пример контекстного менеджера!")

with open('filename.txt', 'r') as f:
    # тут мог бы быть ваш __enter__
    print(f.read())
    # тут мог бы быть ваш __exit__


contextlib.contextmanageer
def my_context():
    # __enter__
    print("enter code")

    yield

    # __exit__
    print("exit code")
