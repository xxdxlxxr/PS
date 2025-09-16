A, B, C, M = map(int, input().split())
tmp, answer = 0, 0

for i in range(24):
  if tmp > M:
    print(0)
  else:
    if tmp + A <= M:
      tmp += A
      answer += B
    else:
      if tmp - C >= 0:
        tmp -= C
      else:
        tmp = 0

print(answer)