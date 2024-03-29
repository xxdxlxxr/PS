N, L = map(int, input().split())
cnt = []

for _ in range(N):
    string = input().split('0')
    cnt.append(len(string) - string.count(''))

print(max(cnt), cnt.count(max(cnt)))