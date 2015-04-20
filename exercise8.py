from time import clock


def naive_fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return naive_fib(n - 1) + naive_fib(n - 2)


def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)


def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n-1, p1, p0 + p1)


start = clock()
result = naive_fib(n)
stop = clock()
difference = (stop - start) * 1000

naive_fib(3)
print difference