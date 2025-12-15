w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
a, b = (p + t) // w, (q + t) // h
print((p + t) % w if a % 2 == 0 else w - (p + t) % w, (q + t) % h if b % 2 == 0 else h - (q + t) % h)