def sum_num(inputs):
    return sum(int(i) for i in inputs if i.isdigit())

for serial in sorted((input() for i in range(int(input()))), key = lambda x:(len(x), sum_num(x), x)):
    print(serial)