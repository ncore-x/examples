class First:
    def __init__(self):
        self._login = "login"
        self.__password = "password"


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = "SuperUser"
        self.__password = "QWERTY"


user_1 = First()
user_2 = Second()

print(user_1._login)
print(user_1._First__password)

print(user_2._login)
print(user_2._Second__password)

print(user_2.__password)

# Output:

# login
# password

# SuperUser
# QWERTY

# AttributeError: 'Second' object has no attribute '__password'

# single underscore(_login) — это соглашение: атрибут помечен как "protected"/внутренний, но на уровне языка он полностью доступен. Такое имя предупреждает других разработчиков, что поле предназначено для внутреннего использования, но Python не запрещает к нему доступ: user._login работает.

# double leading underscore(__password) запускает механизм name mangling: интерпретатор переименовывает атрибут в _ClassName__password внутри класса.

# Рекомендация: используйте один ведущий подчёрк(_) для "внутренних" атрибутов
# двойной подчёрк применяйте только если нужно избежать конфликтов имён в иерархии классов — помните, что это не истинная приватность, а лишь переименование атрибута.
