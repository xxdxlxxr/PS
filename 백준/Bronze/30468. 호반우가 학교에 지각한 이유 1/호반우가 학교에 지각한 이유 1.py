statN = list(map(int, input().split()))

print(max(4 * statN[-1] - sum(statN[:4]), 0))