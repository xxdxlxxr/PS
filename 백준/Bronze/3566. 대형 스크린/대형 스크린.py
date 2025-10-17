import math

rh, rv, sh, sv = map(int, input().split())
min_price = 1000000000

for i in range(int(input())):
    rhi, rvi, shi, svi, pi = map(int, input().split())
    h = max(math.ceil(rh / rhi), math.ceil(sh / shi))
    v = max(math.ceil(rv / rvi), math.ceil(sv / svi))
    min_price = min(min_price, h * v * pi)
    h = max(math.ceil(rh / rvi), math.ceil(sh / svi))
    v = max(math.ceil(rv / rhi), math.ceil(sv / shi))
    min_price = min(min_price, h * v * pi)

print(min_price)