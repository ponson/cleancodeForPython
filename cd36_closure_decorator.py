# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


#Listing 36
def curry(f):
    argc = f.__code__.co_argcount
    print(f"argc={argc}")
    f_args = []
    f_kwargs = {}
    def g(*args, **kwargs):
        nonlocal f_args, f_kwargs
        f_args += args
        f_kwargs.update(kwargs)
        print(f"f_args={f_args}")
        print(f"f_kwargs={f_kwargs}")
        if len(f_args) + len(f_kwargs) == argc:
            return f(*f_args, **f_kwargs) 
        else:
            return g
    return g


@curry
def deco(msg_before, msg_after, f):
    def g(*args, **kwargs):
        print(msg_before + " " + f.__name__)
        result = f(*args, **kwargs)
        print(msg_after + " " + f.__name__)
        return result
    return g

@deco("Starting", "Finished")
def func(x):
    return print(2*x)

func(2)