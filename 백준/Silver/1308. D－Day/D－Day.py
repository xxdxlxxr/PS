from datetime import datetime

y1, m1, d1 = map(int, input().split())
y2, m2, d2 = map(int, input().split())
time = (datetime(y2, m2, d2) - datetime(y1, m1, d1)).days

print('gg' if time >= 365243 else f'D-{time}')