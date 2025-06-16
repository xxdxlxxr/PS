def DFS(L, total):
    global s
    global tmp

    if total > s:
        return

    if L==k:
        if 0 < total <= s:
            tmp.add(total)
    else:
        DFS(L + 1, total + w[L])
        DFS(L + 1, total - w[L])
        DFS(L + 1, total)

k, w, tmp = int(input()), list(map(int, input().split())), set()
s = sum(w)
DFS(0,0)
print(s - len(tmp))