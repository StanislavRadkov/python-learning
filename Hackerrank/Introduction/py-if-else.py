if __name__ == '__main__':
    n = int(input())

    if n % 2 != 0:
        print('Weird')
    elif n in range(2, 6):
        print('Not Weird')
    elif n in range(6, 20):
        print('Not Weird')
    else:
        print('Not Weird')