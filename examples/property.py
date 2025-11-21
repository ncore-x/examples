class BankAccount:
    bank_name = "MyBank"
    total_accounts = 0

    def __init__(self, owner, balance=0):
        self._owner = owner
        self._balance = balance
        BankAccount.total_accounts += 1
        self._account_number = BankAccount.total_accounts

    # PROPERTY - для контроля доступа к атрибутам
    @property
    def balance(self):
        """Геттер для баланса"""
        return self._balance

    @property
    def owner(self):
        """Геттер для владельца"""
        return self._owner

    @owner.setter
    def owner(self, new_owner):
        """Сеттер для владельца с валидацией"""
        if not new_owner or not isinstance(new_owner, str):
            raise ValueError("Имя владельца должно быть непустой строкой")
        self._owner = new_owner

    @property
    def account_number(self):
        """Геттер для номера счета (только чтение)"""
        return self._account_number

    @property
    def is_overdrawn(self):
        """Вычисляемое свойство - проверка отрицательного баланса"""
        return self._balance < 0

    # CLASSMETHOD - методы, работающие с классом в целом
    @classmethod
    def get_bank_info(cls):
        """Возвращает информацию о банке"""
        return f"Банк: {cls.bank_name}, Всего счетов: {cls.total_accounts}"

    @classmethod
    def create_premium_account(cls, owner):
        """Создает премиальный счет с начальным балансом"""
        return cls(owner, balance=1000)

    @classmethod
    def change_bank_name(cls, new_name):
        """Изменяет название банка для всех счетов"""
        cls.bank_name = new_name
        return f"Название банка изменено на: {new_name}"

    # STATICMETHOD - утилитарные методы, не требующие доступа к классу или экземпляру
    @staticmethod
    def validate_amount(amount):
        """Проверяет корректность суммы"""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        return True

    @staticmethod
    def calculate_interest(principal, rate, years):
        """Рассчитывает сложные проценты"""
        return principal * (1 + rate/100) ** years

    @staticmethod
    def format_currency(amount):
        """Форматирует сумму в денежный формат"""
        return f"${amount:,.2f}"

    # Обычные методы экземпляра
    def deposit(self, amount):
        """Пополнение счета"""
        if self.validate_amount(amount):
            self._balance += amount
            return f"Счет пополнен на {self.format_currency(amount)}"

    def withdraw(self, amount):
        """Снятие со счета"""
        if self.validate_amount(amount):
            if amount <= self._balance:
                self._balance -= amount
                return f"Со счета снято {self.format_currency(amount)}"
            else:
                return "Недостаточно средств на счете"

    def transfer(self, amount, target_account):
        """Перевод на другой счет"""
        if self.validate_amount(amount):
            if amount <= self._balance:
                self._balance -= amount
                target_account._balance += amount
                return f"Перевод {self.format_currency(amount)} выполнен успешно"
            else:
                return "Недостаточно средств для перевода"

    def __str__(self):
        return f"Счет #{self.account_number}: {self.owner} - {self.format_currency(self.balance)}"


# Демонстрация использования
if __name__ == "__main__":
    # Создание счетов
    account1 = BankAccount("Иван Иванов", 500)
    account2 = BankAccount.create_premium_account("Петр Петров")

    print(account1)
    print(account2)
    print()

    # Использование property
    print(f"Баланс счета: {account1.balance}")
    print(f"Овердрафт: {account1.is_overdrawn}")

    # Изменение владельца через property setter
    account1.owner = "Иван Сидоров"
    print(f"Новый владелец: {account1.owner}")
    print()

    # Использование classmethod
    print(BankAccount.get_bank_info())
    print(BankAccount.change_bank_name("SuperBank"))
    print(BankAccount.get_bank_info())
    print()

    # Использование staticmethod
    print(f"Форматированная сумма: {BankAccount.format_currency(1234.56)}")

    interest = BankAccount.calculate_interest(1000, 5, 2)
    print(f"Сложные проценты: {BankAccount.format_currency(interest)}")
    print()

    # Операции со счетами
    print(account1.deposit(200))
    print(account1.withdraw(100))
    print(account1.transfer(150, account2))

    print(f"\nИтоговый баланс:")
    print(account1)
    print(account2)
