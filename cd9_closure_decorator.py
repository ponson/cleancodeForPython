# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 9
def f(x):
    z = 2
    def g(y):
        return z*x + y
    return g
a = 5
b = 1
h = f(a)
h(b)  # Output is 11

print(h.__code__.co_freevars)
print(h.__code__.co_freevars[0], "=", h.__closure__[0].cell_contents) 
print(h.__code__.co_freevars[1], "=", h.__closure__[1].cell_contents)