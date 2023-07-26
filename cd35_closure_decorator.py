# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


#Listing 35

def deco(msg_before, msg_after, f):
    def g(*args, **kwargs):
        print(msg_before + " " + f.__name__)
        result = f(*args, **kwargs)
        print(msg_after + " " + f.__name__)
        return result
    return g


def func(x):
    return print(2*x)


func = deco("Starting", "Finished", func)
func(2)