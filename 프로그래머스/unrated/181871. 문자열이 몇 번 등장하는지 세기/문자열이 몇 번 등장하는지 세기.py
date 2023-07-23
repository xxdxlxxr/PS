def solution(myString, pat):
    return sum(pat == myString[i:i + len(pat)] for i in range(len(myString) - len(pat) + 1))