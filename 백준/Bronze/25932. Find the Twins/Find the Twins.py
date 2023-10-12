for _ in range(int(input())):
    nums = list(map(int, input().split()))

    print(*nums)
    print('both' if 18 in nums and 17 in nums else 'mack' if 18 in nums else 'zack' if 17 in nums else 'none')
    print()