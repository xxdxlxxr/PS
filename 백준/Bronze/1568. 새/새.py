N, K, answer = int(input()), 1, 0

while N:
    if K > N:
        K = 1

    N -= K
    K += 1
    answer += 1

print(answer)