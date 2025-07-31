sentence, i, answer = input(), 0, ''

while i < len(sentence):
    answer += sentence[i]
    i += 2 * (sentence[i] in 'aeiou') + 1

print(answer)