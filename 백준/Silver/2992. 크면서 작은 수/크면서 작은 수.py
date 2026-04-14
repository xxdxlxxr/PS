import math
from itertools import permutations

X, answer = input(), math.inf

for i in permutations(X, len(X)):
    tmp = ''

    for j in i:
        tmp += j

    if answer > int(tmp) and int(X) < int(tmp):
        answer = int(tmp)

print(0 if answer == math.inf else answer)