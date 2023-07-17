def show(e, rest):
    print(f"Element: {e} - Rest: {rest}")


# *rest, last = range(10, 1, -1)
# show(last, rest)

def func_key(a=1, b=2, c=3):
    print(f"a={a}, b={b}, c={c}")


func_key(**{'a':8, 'b':9, 'c':7,})