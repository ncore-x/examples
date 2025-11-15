word = "Hello, World!"

ids = set()
# a_list = []

for e in range(10):
    # a_list.append(word) # prints 10
    word = word + str(e)
    ids.add(id(word))

print(len(ids))  # prints 2
