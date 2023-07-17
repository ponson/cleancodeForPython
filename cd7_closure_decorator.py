# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 7
def f(x):
    def g(y):
        return y
    return g
a = 5
b = 1
print(f(a)(b))  # Output is 1