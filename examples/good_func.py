import random

# 1. Имеет читаемое название, нужную информацию получает в артументах
# 2. Читаемая/короткая
# 3. Возвращает результат (не print!)
# 4. Независима (NO GLOBAL), не меняет ничего вне себя


def generate_pin(length: int) -> str:
    return "".join(str(random.randint(0, 9)) for _ in range(length))


def replace_fives(a_list: list, value: str) -> list[str]:
    return [element.replace("5", value) for element in a_list]


def file_write(filename: str, data: str):
    with open(filename, "w") as file:
        file.write(data)


if __name__ == "__main__":
    pins = [generate_pin(8) for _ in range(10)]
    pins_without_fives = replace_fives(pins, "6")
    str_list = "\n".join(pins_without_fives)
    print(pins_without_fives)
    file_write("test2.txt", str_list)
