import file as f
import object_class as o

class Engine:
    def __init__(self, paths=['test_code.py']):
        self.__paths = paths
        self.__files = []
        for path in self.__paths:
            self.__files.append(f.PyLocFile(path))

    def Read(self):
        for file in self.__files:
            file.Read()

    def GetClasses(self):
        classes = []
        #for file in self.__files:
        #    for cl in file.GetClasses():
        #        classes.append(cl)
        classes = [o.ObjectClass('Animal',['point','health','name'],['Heal()','Upgrade()'],[],{}),
                   o.ObjectClass('Weapon',['type','damage'],['Hit()'],[],{}),
                   o.ObjectClass('Shotgun',['bullet','clip'],['Shoot()','Reload()'],['Weapon'],{}),
                   o.ObjectClass('Cat',['weapon','voice'],['Meow()','Kill()'],['Animal'],{'weapon':'Weapon'}),
                   o.ObjectClass('Dog',[],[],['Animal'],{}),
                   o.ObjectClass('Pigeon',[],[],['Animal'],{})]
        return classes
