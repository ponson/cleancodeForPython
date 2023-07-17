# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 5
def f(x):
    def g(y):
        return y
    return g
a = 5
b = 1
h=f(a)
print(h(b))  # Output is 1
print(h.__name__)