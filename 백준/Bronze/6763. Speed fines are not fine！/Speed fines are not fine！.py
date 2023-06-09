limit, speed = int(input()), int(input())

if speed - limit > 30:
    answer = 500
elif speed - limit > 20:
    answer = 270
elif speed - limit > 0:
    answer = 100
else:
    answer = False

print(f'You are speeding and your fine is ${answer}.' if answer else 'Congratulations, you are within the speed limit!')