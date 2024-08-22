n, Gahui = int(input()), int(input())
print(sum(votes > Gahui for votes in map(int, input().split())) + 1)