for names in sorted(sorted([input().split() for _ in range(int(input()))], key=lambda x: x[1], reverse=True), key=lambda x: x[0]):
    print(*names)