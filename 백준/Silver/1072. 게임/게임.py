X, Y = map(int, input().split())
Z, left, right, answer = (100 * Y) // X, 0, X, X

if Z >= 99:
    print(-1)
else:
    while left <= right:
        mid = (left + right) // 2

        if (100 * (Y + mid)) // (X + mid) > Z:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)