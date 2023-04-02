N, a = int(input()), list(map(int, input().split()))
benefit, answer = 0, 0

for i in range(N - 1, -1, -1):
    benefit = max(a[i], benefit)
    answer = max(benefit - a[i], answer)

print(answer)