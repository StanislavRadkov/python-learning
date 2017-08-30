for i in range(0, int(input())):
    try:
        a = list(map(int, input().split()))
        print(a[0]//a[1])
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)