N, cnt = int(input()), input().count('bigdata')

if 2 * cnt == N:
    print('bigdata?', 'security!')
else:
    print(['bigdata?', 'security!'][2 * cnt < N])