if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    arr.reverse()

    print(arr[1])
