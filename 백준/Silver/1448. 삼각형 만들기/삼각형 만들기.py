N = int(input())
length, answer = sorted([int(input()) for _ in range(N)], reverse=True), -1

for i in range(N - 2):
    if length[i] < length[i + 1] + length[i + 2]:
        answer = length[i] + length[i + 1] + length[i + 2]
        break
    
print(answer)