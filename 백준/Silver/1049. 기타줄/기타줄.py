N, M = map(int, input().split())
package, single = [], []

for _ in range(M):
    a, b = map(int, input().split())
    package.append(a)
    single.append(b)

min_package, answer = min(package), 0

while N > 0:
    if N >= 6:
        min_single = min(single)*6
        N -= 6
    else:
        min_single = N * min(single)
        N -= N
        
    if min_single < min_package:
        answer += min_single
    else:
        answer += min_package

print(answer)