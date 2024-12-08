Sab = int(input())
print('high speed rail' if Sab <= max(240, sum(map(int, input().split()))) else 'flight')