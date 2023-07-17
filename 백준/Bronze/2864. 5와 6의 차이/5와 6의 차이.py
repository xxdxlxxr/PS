A, B = input().split()

print(eval(A.replace('6', '5') + '+' + B.replace('6', '5')), eval(A.replace('5', '6') + '+' + B.replace('5', '6')))