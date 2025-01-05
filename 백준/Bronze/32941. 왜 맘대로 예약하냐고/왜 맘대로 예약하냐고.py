T, X = input().split()
answer = 1

for _ in range(int(input())):
    input()

    if X not in input().split():
        answer = 0
        break

print(['NO', 'YES'][answer])