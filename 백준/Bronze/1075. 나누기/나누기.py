N, F = int(input()[:-2] + '00'), int(input())

while N % F:
    N += 1

print(str(N)[-2:])