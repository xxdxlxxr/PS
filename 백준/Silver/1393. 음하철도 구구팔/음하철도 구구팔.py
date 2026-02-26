def get_gcd(a, b):
    while b:
        a, b = b, a % b
        
    return a

xs, ys = map(int, input().split())
xe, ye, dx, dy = map(int, input().split())
gcd = get_gcd(dx, dy)
dx, dy, total_x, total_y = dx // gcd, dy // gcd, xe, ye

while ((total_x - xs) ** 2 + (total_y - ys) ** 2) > (total_x + dx - xs) ** 2 + (total_y + dy - ys) ** 2:
    total_x += dx
    total_y += dy
    
print(total_x, total_y)