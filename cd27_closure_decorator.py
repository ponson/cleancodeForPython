# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 27

def trace(f):
    level = 1
    def helper(*arg):
        nonlocal level
        print((level-1)*"  |", "  ┌",  f.__name__, "(", ",".join(map(str, arg)), ")", sep="")
        level += 1
        result = f(*arg)
        level -= 1
        print((level-1)*"  │", "  └",  result, sep="")
        return result
    return helper


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
fib = trace(fib)
fib(4)