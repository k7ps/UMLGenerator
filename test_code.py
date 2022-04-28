from calendar import c

class B:
    a = 10

class A:
    def __init__(self, a, b):
        self.a:B = a  #!UML A
        self.b = b

class Animal:
    a = 10
    b = 11
    def abc(c):
        return c*2
    def abs(c):
        return c**2
    ab = 2
    # class B:
        # pass

class Grass:
    def __init__(self):
        super().__init__()
        self.b: int = 10
        self.b += 2
    def jump(self):
        pass
    r = 1

class Human(Animal):
    def __init__(self):
        super().__init__()
    c:int = 1
    d = 2

class Bybyzian(Animal, Grass):
    def __init__(self):
        super().__init__()
    c = 1
    d = 2


class ObjectClass:
    name = None
    variables = []
    methods = []
    parents = []
    compositions = []

def afaf():
    class B:
        asfaf = 10
        class D:
            ghu = 2138
            def ok(self):
                print('ok')
    a = B().D()
    a.ok()
