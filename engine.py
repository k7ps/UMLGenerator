import object_class as o

class Engine:
    def __init__(self):
        self.__classes = []

    def Read(self):
        # test
        ex1 = o.ObjectClass('Enemy',['health', 'damage', 'point', 'armor'],['Hit','Die','UpLevel'],[],[])
        for i in range(4):
            self.__classes.append(ex1)

    def GetClasses(self):
        return self.__classes
