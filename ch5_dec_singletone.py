def singleton(myc):
    instances = {}
    def getinstance():
        if myc not in instances:
            instances[myc] = myc()

        return instances[myc]
    return getinstance


@singleton
class MyClass:
    def __init__(self):
        self.name = id(self)
        print(f"MyObjectID is {self.name}")
        

obj1 = MyClass()
obj2 = MyClass()