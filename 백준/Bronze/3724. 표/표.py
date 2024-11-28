for _ in range(int(input())):
    M, N = map(int, input().split())
    mul = [1 for _ in range(M)]

    for _ in range(N):
        nums = list(map(int, input().split()))

        for i in range(M):
            mul[i] *= nums[M - i - 1]

    print(M - mul.index(max(mul)))