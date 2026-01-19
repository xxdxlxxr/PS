for _ in range(int(input())):
    N, nums1, M = int(input()), set(map(int, input().split())), int(input())

    for num in map(int, input().split()):
        print(int(num in nums1))