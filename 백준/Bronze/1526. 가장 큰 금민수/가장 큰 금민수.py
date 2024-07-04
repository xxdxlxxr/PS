for i in range(int(input()), 3, -1):
    for num in str(i):
        if num not in '47':
            break
    else:
        print(i)
        break