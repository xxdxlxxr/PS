n, m, t = map(int, input().split())
max_nm, min_nm, burger, coke, cnt = max(n, m), min(n, m), 0, 10000, 0

while t >= max_nm * cnt:
    tmp_t = t - max_nm * cnt
    tmp_burger = cnt
    tmp_coke = 0
    tmp_burger += tmp_t // min_nm
    tmp_coke += tmp_t % min_nm

    if coke > tmp_coke:
        burger = tmp_burger
        coke = tmp_coke
    elif coke == tmp_coke and burger < tmp_burger:
        burger = tmp_burger
        coke = tmp_coke

    cnt += 1

print(f"{burger} {coke}")