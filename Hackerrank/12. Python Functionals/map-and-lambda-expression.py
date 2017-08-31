cube = lambda x: x ** 3
def fibonacci(n):
    return [fib(x) for x in range(n)]

def fib(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    
    return fib(n-2) + fib(n -1)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
    
    