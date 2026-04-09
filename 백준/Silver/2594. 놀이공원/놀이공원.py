tmp, last, answer = [[600, 600], [1320, 1320]], 600, 0

for _ in range(int(input())):
    start, end = input().split()
    start = int(start[:2]) * 60 + int(start[2:]) - 10
    end = int(end[:2]) * 60 + int(end[2:]) + 10
    tmp.append([start, end])

for run, stop in sorted(tmp):
    answer = max(answer, run - last)
    last = max(last, stop)

print(answer)