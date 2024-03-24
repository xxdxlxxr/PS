arr = [['.' for _ in range(20)] for _ in range(10)]

for _ in range(int(input())):
    seat = input()
    arr[ord(seat[0]) - ord('A')][int(seat[1:]) - 1] = 'o'

for row in arr:
    print(''.join(row))