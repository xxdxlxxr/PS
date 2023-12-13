N, results = int(input()), list(map(int, input().split()))

print('INVALID' if results.count(0) >= N / 2 else 'APPROVED' if sum(results) > 0 else 'REJECTED')