responses = [input() for _ in range(int(input()))]
print(sum(input() == response for response in responses))