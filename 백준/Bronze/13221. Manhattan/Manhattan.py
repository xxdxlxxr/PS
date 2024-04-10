taxi, positions, distances = list(map(int, input().split())), [], []

for _ in range(int(input())):
    positions.append(list(map(int, input().split())))
    distances.append(abs(taxi[0] - positions[-1][0]) + abs(taxi[1] - positions[-1][1]))

print(*positions[distances.index(min(distances))])