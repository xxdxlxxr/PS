a, b = map(int, input().split())

hour = a
minute = b - 45 
if minute < 0 :
    hour -= 1
    if hour == -1 :
        hour = 23
    minute += 60
print(hour, minute)