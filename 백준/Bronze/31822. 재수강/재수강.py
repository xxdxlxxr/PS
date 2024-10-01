subject = input()[:5]
print(sum(input()[:5] == subject[:5] for _ in range(int(input()))))