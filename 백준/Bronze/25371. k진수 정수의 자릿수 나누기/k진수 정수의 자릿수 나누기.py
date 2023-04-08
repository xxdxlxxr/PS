def function(n, q):
    result = ''

    while n > 0:
        n, mod = divmod(n, q)
        result += str(mod)

    return result[::-1]

n, k = map(int, input().split())
sum = 0

for unit in function(n, k).split('0'):
    if unit.isdigit():
        sum += int(unit)

print(function(sum, k))