I = int(input())
print(sum(i for i in range(1, I + 1) if I % i == 0))