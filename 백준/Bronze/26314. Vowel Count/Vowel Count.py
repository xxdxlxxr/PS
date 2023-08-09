for _ in range(int(input())):
    str, cnt = input(), 0

    for char in str:
        cnt += char in 'aeiou'

    print(str)
    print(int(cnt > len(str) - cnt))