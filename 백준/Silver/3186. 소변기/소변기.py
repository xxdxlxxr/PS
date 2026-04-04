import re

K, L, N = map(int, input().split())
nums = input()
arr, answer = [st.end() - 1 for st in re.finditer(K * '1', nums)], []

if len(arr) == 0:
    print("NIKAD")
    exit()

for i in range(len(arr) - 1):
    if nums[arr[i] + 1: arr[i + 1]].find(L * '0') != -1:
        answer.append(nums[arr[i] + 1: arr[i + 1]].find(L * '0') + L + arr[i] + 1)

if nums[arr[len(arr) - 1] + 1:].find(L * '0') != -1:
    answer.append(nums[arr[len(arr) - 1] + 1:].find(L * '0') + L + arr[len(arr) - 1] + 1)
else:
    answer.append(nums.rfind('1') + L + 1)

for num in answer:
    print(num)