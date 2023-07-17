# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 6
def f(x):
    def g(x):
        return x
    return g(x)
a = 5
b = 1
h=f(b) 
# This does not work:
h(b)