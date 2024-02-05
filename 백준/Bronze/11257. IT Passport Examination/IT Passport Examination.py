for _ in range(int(input())):
    inputs = list(map(int, input().split()))

    print(inputs[0], sum(inputs[1:]), 'PASS' if sum(inputs[1:]) >= 55 and inputs[1] >= .3 * 35 and inputs[2] >= .3 * 25 and inputs[3] >= .3 * 40 else 'FAIL')