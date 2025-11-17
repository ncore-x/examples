# Наследование - механизм получения доступа к данным и поведению своего предка и расширению (изменению поведения) классов не меняя код

class Employee:
    def __init__(self, name, salary, bonus):
        self.name = name
        self.salary = salary
        self.bonus = bonus

    def calculate_total_bonus(self):
        return self.salary // 100 * self.bonus

    def __str__(self):
        return f"{self.__class__.__name__} {self.name}, salary: {self.salary}, bonus: {self.bonus}%, total bonus: {self.calculate_total_bonus()}"


class Cleaner(Employee):
    def __init__(self, name):
        super().__init__(name, 15000, 1)
        print(self.salary)


class Manager(Employee):
    def __init__(self, name):
        super().__init__(name, 45000, 15)
        print(self.salary)


class Director(Employee):
    def __init__(self, name):
        super().__init__(name, 150000, 100)
        print(self.salary)

e1 = Cleaner("Светлана Петровна")
e2 = Manager("Мария")
e3 = Director("Дмитрий")

print(e1, e2, e3)

# Output:
# 15000
# 45000
# 150000
# Cleaner Светлана Петровна, salary: 15000, bonus: 1 %, total bonus: 150 Manager Мария, salary: 45000, bonus: 15%, total bonus: 6750 Director Дмитрий, salary: 150000, bonus: 100%, total bonus: 150000
