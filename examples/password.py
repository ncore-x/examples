def strength_password(value: str) -> tuple[str, list[str]]:
    errors = []

    if len(value) < 8:
        errors.append("Пароль должен быть не менее 8 символов.")
    if not any(ch.isdigit() for ch in value):
        errors.append("Пароль должен содержать хотя бы одну цифру.")
    if not any(ch.islower() for ch in value):
        errors.append("Пароль должен содержать хотя бы одну строчную букву.")
    if not any(ch.isupper() for ch in value):
        errors.append("Пароль должен содержать хотя бы одну заглавную букву.")
    if not any(ch in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for ch in value):
        errors.append("Пароль должен содержать хотя бы один специальный символ.")

    if errors:
        return "Слабый пароль", errors
    else:
        return "Сильный пароль", []


if __name__ == "__main__":
    print("Требования к паролю: не менее 8 символов, хотя бы одна цифра, строчные и заглавные буквы, специальный символ.")
    while True:
        pwd = input("Введите пароль для проверки (для выхода введите 'exit'): ")
        if pwd.strip().lower() in ("exit", "quit", "q"):
            print("Выход из программы.")
            break

        status, errors = strength_password(pwd)
        print(status)

        if status != "Сильный пароль":
            print("Недостатки пароля:")
            for err in errors:
                print(f"- {err}")
            continue

        print("Пароль принят.")
        break
