print(sum([int(((i + 1) % sum(map(int, str(i + 1)))) == 0) for i in range(10000000)][:int(input())]))