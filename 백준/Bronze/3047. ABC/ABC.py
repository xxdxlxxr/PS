ABC = list(sorted(map(int, input().split())))
print(*(ABC[ord(order) - ord('A')] for order in input()))