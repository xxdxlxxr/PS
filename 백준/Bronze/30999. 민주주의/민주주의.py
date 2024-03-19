N, M = map(int, input().split())

print(sum(sum(2 * (char == 'O') - 1 for char in input()) > 0 for _ in range(N)))