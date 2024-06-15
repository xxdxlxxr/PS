today = input().split('-')
print(sum(today <= input().split('-') for _ in range(int(input()))))