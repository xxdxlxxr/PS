arr, answer = [int(input()) for _ in range(3)], []
answer.append(arr[1] + 2 * arr[2])
answer.append(arr[0] + arr[2])
answer.append(2 * arr[0] + arr[1])

print(2 * min(answer))