def change(n):
    return [5, 2][n == 5] if n in [2, 5] else n if n in [1, 8] else '?'

W, N = input().split()

if W in 'LR':
    for _ in range(int(N)):
        print(*[change(num) for num in reversed(list(map(int, input().split())))])
else:
    for nums in reversed([list(map(int, input().split())) for _ in range(int(N))]):
        print(*[change(num) for num in nums])