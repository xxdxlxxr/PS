X, Y = list(map(int, input().split())), list(map(int, input().split()))
print('Y' if [X[i] + Y[i] for i in range(5)] == 5 * [1] else 'N')