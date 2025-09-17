for i in range(1, int(input()) + 1):
    B = int(input())
    S = input().replace('O', '0').replace('I', '1')
    print(f"Case #{i}: {"".join(chr(int(S[8 * i:8 * (i + 1)], 2)) for i in range(B))}")