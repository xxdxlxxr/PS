N, M = map(int, input().split())
A, D = map(int, input().split())
Sr, Sc = map(int, input().split())
answer = 'NO...'

if Sr == N and N % 2 != D:
    answer = 'YES!'

print(answer)