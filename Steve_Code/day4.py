import collections
from functools import reduce

passwordList = range(206938, 679128)


increasingPasswords = list(filter(lambda x: list(str(x)) == sorted(list(str(x))), passwordList))

doubleDigitPasswords = list(filter(lambda x: len(set(list(str(x)))) != len(str(x)), increasingPasswords))

largerGroupFilter = list(filter(lambda x: 2 in collections.Counter(list(str(x))).values(), doubleDigitPasswords))

print(len(increasingPasswords), len(doubleDigitPasswords), len(largerGroupFilter))