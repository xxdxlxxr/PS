shifts, work = [4, 6, 4, 10], {}

for _ in range(int(input())):
    for i in range(4):
        workers = input().split()

        for worker in workers:
            if worker != '-':
                if worker not in work:
                    work[worker] = 0

                work[worker] += shifts[i]

tmp = list(work.values())
print('Yes' if len(tmp) == 0 or max(tmp) - min(tmp) < 13 else 'No')