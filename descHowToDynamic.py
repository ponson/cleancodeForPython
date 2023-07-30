#https://docs.python.org/3/howto/descriptor.html

import os

class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname

s = Directory('.')
print(s.size)
w = Directory('..')
print(w.size)