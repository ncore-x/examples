# math/case

def calculate(a, b, operation) -> int | str:
    match operation:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a*b
        case "/":
            return a // b
        case _:
            return f"Не знаю такой операции {operation}"


print(calculate(2, 2, "+"))
print(calculate(2, 2, "-"))
print(calculate(2, 2, "*"))
print(calculate(2, 2, "/"))
