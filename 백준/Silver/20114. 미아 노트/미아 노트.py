N, H, W = map(int, input().split())
answer = N * ['?']

for _ in range(H):
    word = input()

    for i in range(N * W):
        if word[i] != '?':
            answer[i // W] = word[i]

print(''.join(answer))