for _ in range(int(input())):
    print(*(word[::-1] for word in input().split()))