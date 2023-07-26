# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


#Listing 39
def wraps(f):
    def decorator(g):
        def helper(*args, **kwargs):
            return g(*args, **kwargs)
        attributes = ('__module__', '__name__', '__qualname__', '__doc__', '__annotations__')
        for attr in attributes:
            try:
                value = getattr(f, attr)
            except AttributeError:
                pass
            else:
                setattr(helper, attr, value)
        return helper
    return decorator


def memoize(f):
    memo = {}
    @wraps(f)
    def memoized_func(n):
        if n not in memo:            
            memo[n] = f(n)
        return memo[n]
    return memoized_func


@memoize
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


print(fib(6))