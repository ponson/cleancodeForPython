# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6

import time
#Listing 26

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        print(f"c4:fib={fib}")
        return fib(n-1) + fib(n-2)


def memoize(f):
    memo = {}
    def memoized_func(n):
        if n not in memo:
            print(f"c3:f={f}")
            memo[n] = f(n)
        return memo[n]
    return memoized_func

time1 = time.perf_counter()
print(f"c1:fib={fib}")
fib = memoize(fib)
print(f"c2:fib={fib}")
print(fib(100))
time2 = time.perf_counter()
print(f"case 1 time: {time2-time1}")
# for i in range(100):
#     print(fib(i), ' ')
# time3 = time.perf_counter()
# print(f"case 2 time: {time3-time2}")
# (WRNOG!)This algorithm is not good enough. If you just call fib(40), it still has redundents calling fib function.
# You need to use for i in range(40), this is valid to use the effective memoize function than just call fib(40)
# (Correct!) After this line: fib = memoize(fib), the function reference has become
# fib has changed to memoized_func
# f has changed to original fib
# the function name 'fih' in original fih body also has change to reference memoized_func