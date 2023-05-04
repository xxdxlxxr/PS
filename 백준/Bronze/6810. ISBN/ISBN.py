ISBN, answer = '9780921418', 0

for _ in range(3):
    ISBN += input()

for i in range(13):
    answer += int(ISBN[i]) * (2 * (i % 2) + 1)

print('The 1-3-sum is', answer)