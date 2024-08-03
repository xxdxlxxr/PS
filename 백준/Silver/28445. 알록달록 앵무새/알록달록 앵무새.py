colors = sorted(set(input().split() + input().split()))

for color_1 in colors:
    for color_2 in colors:
        print(color_1, color_2)