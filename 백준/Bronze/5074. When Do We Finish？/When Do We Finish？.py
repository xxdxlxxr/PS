while 1:
    start, duration = input().split()
    start, duration = list(map(int, start.split(':'))), list(map(int, duration.split(':')))

    if sum(start) + sum(duration) == 0:
        break

    answer = [start[0] + duration[0], start[1] + duration[1]]

    if answer[1] > 59:
        answer[0] += 1
        answer[1] -= 60

    print(f'{answer[0] % 24:02d}:{answer[1]:02d}', f'+{answer[0] // 24}' if answer[0] // 24 else '')