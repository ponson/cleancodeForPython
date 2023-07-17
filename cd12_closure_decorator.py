# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 12
def f(x):
    def g(y = x):
        return y
    return g
a = 5
b = 1
h = f(a)
h()  # Output is 5
print(h.__code__.co_freevars)
print(h.__closure__)