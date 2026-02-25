num = bin(int(input()))[2:]
print(sum(3 ** (len(num) - i - 1) for i in range(len(num)) if num[i] == '1'))