# https://towardsdatascience.com/closures-and-decorators-in-python-2551abbc6eb6


# Listing 19
def partial(f, *f_args, **f_keywords):
    def g(*args, **keywords):
        new_keywords = f_keywords.copy()
        new_keywords.update(keywords)
        return f(*(f_args + args), **new_keywords)
    return g


# Listing 20
func = lambda x,y,z: x**2 + 2*y + z
pfunc = partial(func, 1)
pfunc(2, 3)  # Output is 8