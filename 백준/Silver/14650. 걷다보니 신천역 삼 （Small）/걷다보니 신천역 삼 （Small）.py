N, answer = int(input().rstrip()), 0

def function(n, sum):
    global answer

    for i in range(3):
        if n == 0 and i == 0:
            continue

        if n == N:
            if sum % 3 == 0:
                answer += 1
                return answer
        else:
            function(n + 1, int(str(sum + i)))

function(0,0)
print(answer)