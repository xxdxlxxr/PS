arr = [int(input()) for _ in range(int(input()))]
answer = set(range(1, max(arr) + 1)) - set(arr)

if answer:
    for number in sorted(answer):
        print(number)
else:
    print('good job')