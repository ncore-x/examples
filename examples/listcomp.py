# listcomp
listcomp = [e ^ 2 for e in range(10) if e % 2 == 0]
print(listcomp)

# dictcomp
dictcomp = {e: e ^ 2 for e in range(10) if e % 2 == 0}
print(dictcomp)

# genexp
genexp = (e for e in range(100) if e % 2 == 0)
print(next(genexp))
print(next(genexp))
print(next(genexp))
