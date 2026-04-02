import math

for i in str(math.factorial(int(input())))[::-1]:
    if i == '0':
        continue
    else:
        print(i)
        break