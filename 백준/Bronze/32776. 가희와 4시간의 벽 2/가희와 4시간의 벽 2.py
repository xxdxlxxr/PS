Sab = int(input())
print('high speed rail' if Sab <= 240 or Sab <= sum(map(int, input().split())) else 'flight')