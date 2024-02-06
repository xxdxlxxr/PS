for _ in range(int(input())):
    ud = input()

    print(ud.find('D') if 'D' in ud else len(ud))