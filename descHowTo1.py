class Ten:
    def __get__(self, obj, objtype=None):
        return 10


class A:
    x = 5
    y = Ten()


a = A()
print(a.x)
print(a.y)