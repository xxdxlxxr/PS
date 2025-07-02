N, M = map(int, input().split())
lowercase, q, r = [''] + [chr(i) for i in range(ord('a'), ord('z') + 1)], M // 26, M % 26
print(f'SN {N}{lowercase[M].upper() if M <= 26 else lowercase[q - 1] + lowercase[-1] if r == 0 else lowercase[q] + lowercase[r]}')