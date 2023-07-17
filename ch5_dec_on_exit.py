def onexit(f):
    import atexit
    atexit.register(f)
    return f
    

@onexit
def func():
    print("Hello, Decorator 1.")
    
