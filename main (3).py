if __name__ == '__main__':
    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])
    middle = 1
    temp = m
    for i in range(n//2):
        j = 0
        while j < m:
            if ((temp // 2) - 1) == j:
                for _ in range(middle):
                    print('.|.', end = '')
                j = j + middle * 3
                middle += 2
            else:
                print('-', end = '')
                j += 1
        temp -= 6
        print()

    i = 0
    while i < m:
        if ((m - 7) // 2) == i:
            print('WELCOME', end = '')
            i = i + 7
        else:
            print('-', end = '')
            i += 1
    print()
    temp += 6
    middle -= 2    
    for i in range(n//2):
        j = 0
        while j < m:
            if ((temp // 2) - 1) == j:
                for _ in range(middle):
                    print('.|.', end = '')
                j = j + middle * 3
                middle -= 2
            else:
                print('-', end = '')
                j += 1
        temp += 6
        print()


    





