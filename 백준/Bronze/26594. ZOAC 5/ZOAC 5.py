string, answer = input(), 1

for i in range(len(string) - 1):
    if string[i] == string[i+1]:
        answer += 1
    else :
        break

print(answer)