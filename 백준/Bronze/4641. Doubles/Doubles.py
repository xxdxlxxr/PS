while 1:
    nums = list(map(int, input().split()))[:-1]

    if not len(nums):
        break

    print(sum(2 * num in nums for num in nums))