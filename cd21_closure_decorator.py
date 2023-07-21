# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


#Listing 21

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


func = lambda x,y,z: x**2 + 2*y + z
cfunc = curry(func)
print(cfunc(x=1)(y=2))
print(cfunc(z=3))