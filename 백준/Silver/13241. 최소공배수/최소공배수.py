A, B = map(int, input().split())
answer = A * B

while B:
    if A > B:
        A, B = B, A

    B %= A

print(answer // A)