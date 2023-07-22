def solution(myString, pat):
    for i in range(len(myString) - len(pat) + 1):
        if pat in myString[-(i + len(pat)):][:len(pat)]:
            return myString[:len(myString) - i]