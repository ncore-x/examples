class Duck:
    def quack(self):
        return "Кря!"

    def walk(self):
        return "Утка идёт вперевалку"

class Person:
    def quack(self):
        return "Я тоже могу крякнуть!"

    def walk(self):
        return "Человек идёт пешком"

duck = Duck()
person = Person()

# Функция не зависит от типа объекта.
# Ей важно только то, что у объекта есть методы quack и walk.
def make_it_quack_and_walk(arg):
    return arg.quack(), arg.walk()


print(make_it_quack_and_walk(duck))
print(make_it_quack_and_walk(person))

# Python не важно, к какому типу относится объект.
# Важно то, какие методы у него есть.
# Функция make_it_quack_and_walk работает и с уткой, и с человеком, потому что у обоих есть методы quack и walk.

# Это и есть Duck Typing:
# «Если объект выглядит как утка, плавает как утка и крякает как утка — значит, это утка.»
