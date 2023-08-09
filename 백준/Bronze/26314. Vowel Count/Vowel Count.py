for _ in range(int(input())):
    str = input()
    cnt = sum([char in 'aeiou' for char in str])
    
    print(str)
    print(int(cnt > len(str) - cnt))