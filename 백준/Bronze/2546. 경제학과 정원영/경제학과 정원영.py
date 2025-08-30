for t in range(int(input())):
    input()
    N, M = map(int, input().split())
    C_IQ, E_IQ = list(map(int, input().split())), list(map(int, input().split()))
    C_avg, E_avg = sum(C_IQ) / N, sum(E_IQ) / M
    print(sum(c < C_avg and c > E_avg for c in C_IQ))