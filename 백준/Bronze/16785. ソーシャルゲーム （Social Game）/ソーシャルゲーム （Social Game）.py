A, B, C = map(int, input().split())

print(C // (7 * A + B) * 7 + min(-(C % (7 * A + B) // -A), 7))