N, M = map(int, input().split())
rotate, arr = [46, 79, 124, 45, 92, 47, 60, 118, 62, 94], ['' for _ in range(M)]

for _ in range(N):
    string = input()

    for i in range(M):
        arr[M - i - 1] += chr(rotate['.O-|/\^<v>'.index(string[i])])

print('\n'.join(arr))