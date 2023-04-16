K, R, N = input().split()
King, Rock = [ord(K[0]) - 65, int(K[1]) - 1], [ord(R[0]) - 65, int(R[1]) - 1]

def move(location, direction):
    before = location

    for unit in direction:
        if unit == 'R':
            location = [location[0] + 1, location[1]]
        elif unit == 'L':
            location = [location[0] - 1, location[1]]
        elif unit == 'B':
            location = [location[0], location[1] - 1]
        else:
            location = [location[0], location[1] + 1]

    if min(location[0], location[1]) < 0 or max(location[0], location[1]) > 7:
        return before
    else:
        return location

for i in range(int(N)):
    where = input()

    King_before, King_after, Rock_before = King, move(King, where), Rock

    if King_after == Rock_before:
        Rock_after = move(Rock_before, where)

        if Rock_before == Rock_after:
            King = King_before
            Rock = Rock_before
        else:
            King = King_after
            Rock = Rock_after
    else:
        King = King_after

print(chr(King[0] + 65) + str(King[1] + 1))
print(chr(Rock[0] + 65) + str(Rock[1] + 1))