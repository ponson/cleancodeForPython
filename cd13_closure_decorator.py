# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 13
def f(x):
    def g(y):
        def h(z):
            return x * y * z
        return h
    return g
a = 5
b = 2
c = 1
f(a)(b)(c)  # Output is 10
print(f(a)(b).__code__.co_freevars)
print(f(a).__code__.co_freevars)