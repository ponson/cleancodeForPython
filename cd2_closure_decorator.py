# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 2
a = [1, 2, 3]
b = 5
def func(x, y):
    x.append(4)
    y = y + 1
func(a, b)
print("a=", a)  #  Output is a=[1, 2, 3, 4]
print("b=", b)  #  Output is b=5