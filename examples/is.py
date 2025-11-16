first_word = "python"
second_word = "python"
third_word = "pyt" + "hon"

first_value = "pyt"
second_value = first_value + "hon"

print(first_word is second_word, first_word is third_word, first_value is second_value)  # True, True, False

first_big_int = 10_000
second_big_int = int("10000")

print(first_big_int is second_big_int)  # False, different integer objects despite having the same value

# Small integers between -5 and 256 are cached by Python
first_smoll_int = 100
second_smoll_int = int("100")

print(first_smoll_int is second_smoll_int)  # True, small integers are cached by Python
