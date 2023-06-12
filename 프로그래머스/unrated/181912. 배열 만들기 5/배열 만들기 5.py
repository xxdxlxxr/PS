def solution(intStrs, k, s, l):
    return [int(intStr[s:s + l]) for intStr in intStrs if int(intStr[s:s + l]) > k]