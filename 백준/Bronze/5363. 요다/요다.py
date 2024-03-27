for _ in range(int(input())):
    words = input().split()
    print(*words[2:], *words[:2])