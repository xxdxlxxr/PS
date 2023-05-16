def solution(ineq, eq, n, m):
    if eq == '=' and n == m:
        return 1
    else:
        return int((ineq == '>' and n > m) or (ineq == '<' and n < m))