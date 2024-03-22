input()
count = 26 * [0]

for char in input():
    if char.isalpha():
        count[ord(char) - ord('a') + 1] += 1

print(max(count))