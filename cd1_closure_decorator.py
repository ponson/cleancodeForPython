# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 1
x = 1 # x is a global variable  
y = 5 # y is a global variable 
def f():
    global y 
    x = 2   # x is a local variable
    y += 1  # Reassigning the global variable y
    z = 10   # z is a local variable
    print("Local variable x =", x)
    print("Global variable y =", y)
    print("Local variable z =", z)
f()
print("Global variable x =", x)
print("Global variable y =", y)