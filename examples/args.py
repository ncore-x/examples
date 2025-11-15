def count(word: str, count: dict = {}) -> dict:  # dict is mutable default argument
    for letter in word:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    return count


count("A")  # {"A": 1}
print(count("BC"))  # res = {'A': 1, 'B': 1, 'C': 1}
