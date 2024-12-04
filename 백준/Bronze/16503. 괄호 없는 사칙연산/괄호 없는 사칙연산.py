K1, O1, K2, O2, K3 = input().split()
result = (int(eval(str(int(eval('(' + K1 + O1 + K2 + ')'))) + O2 + K3)), int(eval(K1 + O1 + str(int(eval('(' + K2 + O2 + K3 + ')'))))))
print(min(result))
print(max(result))