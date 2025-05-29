files = {}

for i in range(int(input())):
    _, extend = input().split('.')

    if extend in files:
        files[extend] += 1
    else:
        files[extend] = 1

for key in sorted(files):
    print(key, files[key])