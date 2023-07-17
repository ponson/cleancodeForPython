# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 11
def f(x):
    z = 2
    t = 3
    def g(y):
        nonlocal t
        return y
    return g
a = 5
b = 1
h = f(a)
print(h(b))
# 
print(h.__code__.co_freevars)
