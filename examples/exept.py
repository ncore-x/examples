def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    except TypeError:
        return "Оба аргумента должны быть числами"


print(safe_divide(10, 0))


def to_int(value):
    try:
        res = int(value)
        return res
    except (ValueError, TypeError):
        return "Невозможно преобразовать в число"
    finally:
        print("Готово")


print(to_int(100))


def get_item(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Индекс вне диапазона"
    except TypeError:
        return "Ожидался список"


print(get_item(["a", "b", "c", "d", "e"], 2))


def to_list(value):
    try:
        return list(value)
    except TypeError:
        return "Нельзя преобразовать в список"


print(to_list(None))


def smart_divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Оба аргумента должны быть числами"

    try:
        return a / b
    except ZeroDivisionError:
        return "Нельзя делить на ноль"


print(smart_divide(1, 2))


def read_file_safe(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        return "Файл не найден"
    finally:
        print("Попытка чтения файла завершена")


print(read_file_safe("exa123.txt"))


def logged_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    finally:
        print(f"Выполнено деление {a} на {b}")


print(logged_divide(1, 2))


def safe_int(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return "Невозможно преобразовать в число"
    finally:
        print("Попытка преобразования завершена")


print(safe_int("a"))


def get_dict_value(d, key):
    if not isinstance(d, dict):
        return "Ожидался словарь"
    try:
        return d[key]
    except KeyError:
        return "Ключ не найден"
    finally:
        print(f"Попытка получить значение завершена")


get_dict_value({"a": 1, "b": 2}, "b")
get_dict_value({"a": 1}, "c")
get_dict_value([1, 2, 3], 1)


def sum_list_elements(lst):
    if not isinstance(lst, list):
        return "Ожидался список"
    try:
        return sum(lst)
    except TypeError:
        return "Список должен содержать только числа"
    finally:
        print("Попытка посчитать сумму завершена")


print(sum_list_elements([1, 2, 3]))
print(sum_list_elements([1, "a", 3]))
print(sum_list_elements("123"))


def divide_numbers(numbers, divisor):
    if not isinstance(numbers, list) or not isinstance(divisor, (int, float)):
        return "Неверные типы аргументов"
    try:
        return [num / divisor for num in numbers]
    except TypeError:
        return "Список должен содержать только числа"
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    finally:
        print("Попытка выполнить деление завершена")


print(divide_numbers([10, 20, 30], 2))
print(divide_numbers([10, "a", 30], 2))
print(divide_numbers([10, 20], 0))
print(divide_numbers("123", 2))

print("#")

def update_dict_values(d, divisor):
    if not isinstance(d, dict) or not isinstance(divisor, (int, float)):
        return "Неверные типы аргументов"
    try:
        for key in d:
            d[key] = d[key] / divisor
        return d
    except TypeError:
        return "Словарь должен содержать только числа"
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    finally:
        print("Попытка обновления словаря завершена")


print(update_dict_values({"a": 10, "b": 20}, 2))
print(update_dict_values({"a": 10, "b": "x"}, 2))
print(update_dict_values({"a": 10, "b": 20}, 0))
print(update_dict_values([1, 2, 3], 2))

print("#")


def safe_divide_dicts(dict_list, divisor):
    if not isinstance(dict_list, list) or not isinstance(divisor, (int, float)):
        return "Неверные типы аргументов"
    try:
        result = []
        for lst in dict_list:
            if not isinstance(lst, dict):
                return "Список должен содержать только словари"
            new_lst = {}
            for key, value in lst.items():
                new_lst[key] = value / divisor
            result.append(new_lst)
        return result
    except TypeError:
        return "Словарь должен содержать только числа"
    except ZeroDivisionError:
        return "Нельзя делить на ноль"
    finally:
        print("Попытка деления завершена")


print(safe_divide_dicts([{"a": 10, "b": 20}, {"x": 30}], 2))
# [{"a": 5.0, "b": 10.0}, {"x": 15.0}], и печатает сообщение

print(safe_divide_dicts([{"a": 10, "b": "x"}], 2))
# "Словарь должен содержать только числа", и печатает

print(safe_divide_dicts([{"a": 10}, 123], 2))
# "Список должен содержать только словари", и печатает

print(safe_divide_dicts([{"a": 10}], 0))
# "Нельзя делить на ноль", и печатает


def safe_nested_divide(dict_list, divisor):
    if not isinstance(dict_list, list) or not isinstance(divisor, (int, float)):
        return "Неверные типы аргументов"

    try:
        result = []
        for d in dict_list:
            if not isinstance(d, dict):
                return "Список должен содержать только словари"

            new_d = {}
            for key, value in d.items():
                if not isinstance(value, (int, float)):
                    return "Словарь должен содержать только числа"
                new_d[key] = value / divisor
            result.append(new_d)

        return result

    except ZeroDivisionError:
        return "Нельзя делить на ноль"

    finally:
        print("Попытка деления завершена")


print(safe_nested_divide([{"a": 10, "b": 20}, {"x": 30, "y": 40}], 2))
print(safe_nested_divide([{"a": 10, "b": "x"}], 2))
print(safe_nested_divide([{"a": 10}, 123], 2))
print(safe_nested_divide([{"a": 10}], 0))
