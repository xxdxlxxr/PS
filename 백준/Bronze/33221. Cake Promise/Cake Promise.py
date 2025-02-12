t, p = map(int, input().split())
Wright = input().split()
sol, tot, answer = sum(m.isnumeric() for m in Wright), sum(int(m) for m in Wright if m.isnumeric()), 0

for _ in range(t - 1):
    other = input().split()
    sol_tmp = sum(m.isnumeric() for m in other)
    answer += sol_tmp > sol or sol_tmp == sol and sum(int(m) for m in other if m.isnumeric()) <= tot

print(answer)