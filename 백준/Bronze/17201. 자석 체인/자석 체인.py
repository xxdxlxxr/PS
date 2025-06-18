N, a, answer = int(input()), input(), 'Yes'

for i in range(0, len(a)- 2, 2):
    if a[i] != a[i + 2]:
        answer = 'No'
        break

print(answer)