N, seats = int(input()), input()
cnt = seats.count('LL')
print(len(seats) + (cnt > 1) * (1 - cnt))