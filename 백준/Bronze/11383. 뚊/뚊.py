N, M = map(int, input().split())
arr, answer = [input() for _ in range(N)], 0

for i in range(N):
    if ''.join(2 * char for char in arr[i]) != input():
        answer = not(answer)
        break

print(answer * 'Not ' + 'Eyfa')