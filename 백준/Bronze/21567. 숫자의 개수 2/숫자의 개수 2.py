A, B, C = int(input()), int(input()), int(input())
answer = 10 * [0]

for num in str(A * B * C):
    answer[int(num)] += 1

for cnt in answer:
    print(cnt)