N, A = int(input()), list(map(int, input().split()))
max_age, min_age = max(A), min(A)

for age in A:
    print(max(abs(max_age - age), abs(min_age - age)))