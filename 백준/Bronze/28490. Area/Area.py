arr = []

for _ in range(int(input())):
    h, w = map(int, input().split())
    arr.append(h * w)

print(max(arr))