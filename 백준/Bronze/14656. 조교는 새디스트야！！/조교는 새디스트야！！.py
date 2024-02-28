N = int(input())
numbers = list(map(int, input().split()))

print(sum(i + 1 != numbers[i] for i in range(N)))