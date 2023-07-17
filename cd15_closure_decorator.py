# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 15

def f(x):
    z = 2
    return lambda y: z*x+y
a = 5
b = 3
print(f(a)(b))