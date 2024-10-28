input()
cnt = sum(2 * (int(num) % 2) - 1 for num in input())
print((cnt // abs(cnt) + 1) // 2 if cnt else -1)