class NthRoot:
    def __init__(self, n=2):
        self.n = n
    def set_root(self, n):
        self.n = n
    def calc(self, x):
        return x ** (1/self.n)


thirdRoot = NthRoot(3)
print(thirdRoot.calc(27)) #Output is 3

def nth_root(n=2):
    def calc(x):
        return x ** (1/n)
    return calc


third_root = nth_root(3)
print(third_root(27)) #Output is 3