memo, type, S = ['fdsajkl;', 'jkl;fdsa', 'asdf;lkj', ';lkjasdf', 'asdfjkl;', '', ';lkjfdsa', ''], ['in-out', 'out-in', 'stairs', 'reverse'], input()

print(type[memo.index(S) // 2] if S in memo else 'molu')