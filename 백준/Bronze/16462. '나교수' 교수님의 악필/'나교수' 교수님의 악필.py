N = int(input())
arr = [min(int(''.join('9' if num in '069' else num for num in input())), 100) for _ in range(N)]

print(int(sum(arr) / N) + (sum(arr) / N - int(sum(arr) / N) >= .5))