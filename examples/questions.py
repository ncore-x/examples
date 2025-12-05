import logging

# Настройка логирования в файл
logging.basicConfig(
    filename="app.log",           # имя файла
    level=logging.INFO,           # уровень логирования
    format="%(asctime)s — %(levelname)s — %(message)s"
)


def file_logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Вызов функции: {func.__name__}")
        logging.info(f"Аргументы: args={args}, kwargs={kwargs}")
        try:
            result = func(*args, **kwargs)
            logging.info(f"Результат: {result}")
            return result
        except Exception as e:
            logging.error(f"Ошибка в функции {func.__name__}: {e}")
            raise
    return wrapper


@file_logger
def divide(a, b):
    return a // b
