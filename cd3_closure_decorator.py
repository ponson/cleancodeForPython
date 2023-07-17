# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 3
def f(x):
    y = 5
    z = 10
    t = 10
    def g():
        nonlocal y
        y += 1
        z = 20
        print("Nonlocal variable x =", x)
        print("Local variable z =", z) 
    print("Local variable t =", t)    
    g()
    print("Nonlocal variable x =", x)
    print("Nonlocal variable y =", y)
    print("Local variable z =", z)
f(5)
# This does not work:
# g()