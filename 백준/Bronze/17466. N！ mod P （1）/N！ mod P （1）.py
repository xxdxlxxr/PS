N, P = map(int, input().split())
answer = 1

for i in range(2, N + 1):
    answer = (answer * i) % P

print(answer % P)