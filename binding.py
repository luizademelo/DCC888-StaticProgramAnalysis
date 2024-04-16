class A:
    def __init__(self):
        self.x = 0
    def get(self, term):
        return self.x + term
class B:
    def __init__(self, start):
        self.x = start
    def get(self, factor):
        return self.x * factor
class C:
    def __init__(self):
        self.x = -1
    def get(self):
        return self.x
    
def foo1(obj):
    return obj.x

def foo2(obj, factor):
    return obj.x * factor
def bar(obj1, obj2):
    return obj1.get() + obj2.get(2.0)
 
a = A()
if int(input("Enter: ")) > 1:
    a = B(1)
    B.get = foo1
c = C()
C.get = foo2
bar(a, c)