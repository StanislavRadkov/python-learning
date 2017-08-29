if __name__ == '__main__':
    def average(array):
        s = set(array)
        return sum(s)/len(s)

    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)