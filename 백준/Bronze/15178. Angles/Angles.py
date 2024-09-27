for _ in range(int(input())):
    angles = list(map(int, input().split()))
    print(*angles, 'Seems OK' if sum(angles) == 180 else 'Check')