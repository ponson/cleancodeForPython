from functools import wraps
def accepts(*types):
    def check_accepts(f):
        print(f"types len:{len(types)}")
        print(f"f.name={f.__name__}")
        print(f"coargcount len: {f.__code__.co_argcount} ")
        print(f"conlocals len: {f.__code__.co_nlocals} ")
        # assert len(types) == f.__code__.co_argcount
        @wraps(f)
        def new_f(*args, **kwds):
            for (a, t) in zip(args, types):
                print(f"a={a}, t={t}")
                assert isinstance(a, t), "arg %r does not match %s" % (a, t)
            return f(*args, **kwds)
        new_f.__name__ = f.__name__
        return new_f
    return check_accepts

def returns(rtype):
    def check_returns(f):
        @wraps(f)
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            assert isinstance(result, rtype), "return value %r does not match %s" % (result, rtype)
            return result
        new_f.__name__ = f.__name__
        return new_f
    return check_returns

@accepts(int, (int, float))
@returns((int, float))
def func(arg1, arg2):
    print(f"no deco, coarg count: {func.__code__.co_argcount}")
    return arg1 * arg2
    

def coargtest(s, y, x):
    # print(f"testcount types len:{len(types)}")
    print(f"testcount len: {coargtest.__code__.co_argcount} ")
    print(f"testlocals len: {coargtest.__code__.co_nlocals} ")

    return


print(func(3, 6.4))
coargtest(1, 2, 3)