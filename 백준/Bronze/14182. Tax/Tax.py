while 1:
    income = int(input())

    if not income:
        break

    print(int(.8 * income) if income > 5000000 else int(.9 * income) if income > 1000000 else income)