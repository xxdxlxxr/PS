for _ in range(int(input())):
    print(['ON', 'OFF'][int(input()) % 25 > 16] + 'LINE')