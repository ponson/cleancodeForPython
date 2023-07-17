# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


def compose(g, f):
    def h(*args, **kwargs):
        return g(f(*args, **kwargs))
    return h


def add2(num1, num2):
    return num1+num2, num1-num2


def mult2(tups):
    return tups[0]*tups[1]


inch_to_foot = lambda x: x/12
foot_meter = lambda x: x * 0.3048

compositeh = compose(mult2, add2)
print(compositeh(10, 5))
# print(add2(10, 5))

inch_to_meter = compose(foot_meter, inch_to_foot)
print(inch_to_meter(12))