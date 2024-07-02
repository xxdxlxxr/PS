N, A = int(input()), sorted([0] + list(map(int, input().split())))

for i in range(N):
    if A[i] + 1 != A[i + 1]:
        print(A[i] + 1)
        break
else:
    print(A[-1] + 1)