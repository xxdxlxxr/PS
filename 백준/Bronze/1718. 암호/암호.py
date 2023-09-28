str1, str2, answer = input(), input(), ''

print(''.join(' ' if str1[i] == ' ' else chr(ord(str1[i]) - ord(str2[i % len(str2)]) + ord('a') - 1 + 26 * (ord(str1[i]) - ord(str2[i % len(str2)]) + ord('a') - 1 < ord('a'))) for i in range(len(str1))))