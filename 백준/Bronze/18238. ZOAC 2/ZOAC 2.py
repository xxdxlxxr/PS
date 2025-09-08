start, end, answer = 'A', 0, 0

for char in input():
  left = ord(start) - ord(char)
  right = ord(char) - ord(start)

  if left < 0:
    left += 26
  elif right < 0:
    right += 26

  answer += min(left, right)
  start = char

print(answer)