# listcomp
listcomp = [e ^ 2 for e in range(10) if e % 2 == 0]
print(listcomp)

# dictcomp
dictcomp = {e: e ^ 2 for e in range(10) if e % 2 == 0}
print(dictcomp)

# dictcomp
assessments = {"неуд.": 2, "уд.": 3, "хор.": 4, "отл.": 5}
upper_assessments = {k.upper(): v for k, v in assessments.items()}
print(upper_assessments)

# genexp
genexp = (e for e in range(100) if e % 2 == 0)
print(next(genexp))
print(next(genexp))
print(next(genexp))
