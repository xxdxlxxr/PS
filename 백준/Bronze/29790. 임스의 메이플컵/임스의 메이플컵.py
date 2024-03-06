N, U, L = map(int, input().split())

print('Bad' if N < 1000 else (U >= 8000 or L >= 260) * 'Very ' + 'Good')