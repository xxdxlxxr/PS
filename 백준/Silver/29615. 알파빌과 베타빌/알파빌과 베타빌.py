N, M = map(int, input().split())
citizen, friends = input().split(), input().split()

print(sum(c not in friends for c in citizen[:M]))