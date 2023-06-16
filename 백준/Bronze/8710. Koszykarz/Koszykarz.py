k, w, m = map(int, input().split())

print((w - k) // m + 1 if (w - k) % m else (w - k) // m)