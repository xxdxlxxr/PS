records = {}

for _ in range(int(input())):
    record = input().split()

    if record[1] == 'enter':
        records[record[0]] = True
    else:
        del records[record[0]]

for name in sorted(records.keys(), reverse=True):
    print(name)