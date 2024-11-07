total = 0

for _ in range(10):
    score = int(input())
    total += score

    if total >= 100:
        print(total if 2 * total <= score + 200 else total - score)
        break
else:
    print(total)