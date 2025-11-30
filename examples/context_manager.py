# Менеджер контекста - это объект Python, который создает временный контекст и ликвидирует его после выполнения функции
# Менеджеры контекста применяются для открытия и закрытия файлов, коннектов к ресурсам, сессиям и др.
# Менеджер контекста гарантирует, что после работы с ресурсом контекст будет ликвидирован, а также, что в случае возникновения исключений контекст также будет закрыт


from contextlib import contextmanager


class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()


# Декоратор contextlib
# C помощью декоратора contextmanager из contextlib можно определить контекст менеджер из генератора, вместо написания класса:

@contextmanager
def open_file(name):
    f = open(name, "w")
    yield f
    f.close()
