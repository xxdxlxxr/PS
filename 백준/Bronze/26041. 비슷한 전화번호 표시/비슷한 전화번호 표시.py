A = input().split()
B = input()

print(sum(nums[:len(B)] == B and len(nums) > len(B) for nums in A))