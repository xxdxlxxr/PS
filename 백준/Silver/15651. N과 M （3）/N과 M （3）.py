N, M = map(int, input().split())
arr = M * [0]

def function(level):
    if level == M:
        print(*arr)

        return 0

    for i in range(N):
        arr[level] = i + 1
        function(level + 1)

function(0)