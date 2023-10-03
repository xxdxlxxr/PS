A, B, C = map(int, input().split())

print(7 * (C // (7 * A + B)) + C % (7 * A + B) if B else C // A + (C % A != 0))