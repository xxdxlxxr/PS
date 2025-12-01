sell = {}

for i in range(int(input())):
    name = input()

    if name not in sell:
        sell[name] = 1
    else:
        sell[name] += 1

best, max_value = [], max(sell.values())

for key, value in sell.items():
    if value == max_value:
        best.append(key)

print(sorted(best)[0])