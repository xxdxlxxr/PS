for _ in range(int(input())):
    nums, sum_odd = list(map(int, input().split()))[1:], 0

    for num in nums:
        sum_odd += (num % 2) * num

    sum_even = sum(nums) - sum_odd

    print((sum_odd < sum_even) * 'EVEN' + (sum_odd > sum_even) * 'ODD' + (sum_odd == sum_even) * 'TIE')