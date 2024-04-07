class A:
    def __init__(self):
        self.x = 0
    def get(self):
        return self.x
    
class B:
    def __init__(self, start):
        self.x = start
    def get(self):
        return self.x
    def inc(self):
        self.x += 1

def foo(obj):
    return obj.x

def bar(obj):
    return obj.get()


def create_binding(obj): 
    if type(obj) == A: 
        print(obj.get())

obj = A()

create_binding(obj)