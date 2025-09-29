A, B, C = map(int, input().split())

if (A == 1 and B == C == 0) or (A == 0 and B == C == 1):
    print("A")
elif (B == 1 and A == C == 0) or (B == 0 and A == C == 1):
    print("B")
elif (C == 1 and A == B == 0) or (C == 0 and A == B == 1):
    print("C")
else:
    print("*")