X = [int(input()) for _ in range(int(input()))]
sorted_X = sorted(X)
print('ez' if X[0] == sorted_X[0] else 'hard' if X[0] == sorted_X[-1] else '?')