while 1:
    balance, WD, amount = input().split()
    balance, amount = int(balance), int(amount)

    if not balance and WD == 'W' and not amount:
        break

    answer = balance + (2 * (WD == 'D') - 1) * amount
    print('Not allowed' if answer < -200 else answer)