from file import *
from object_class import *

class Engine:
    def __init__(self, paths=['test_code.py']):
        self.__paths = paths
        self.__files = []
        for path in self.__paths:
            self.__files.append(PyLocFile(path))

    def Read(self):
        for file in self.__files:
            file.Read()

    def GetClasses(self):
        #return self.__example()
        classes = []
        for file in self.__files:
            for cl in file.GetClasses():
                classes.append(cl)
        return classes

    def __example(self):
        classes = [ObjectClass('Animal',['point','health','name','Heal()','Upgrade()'],ClassInteraction([],{},{},[])),
                   ObjectClass('Weapon',['type','damage','Hit()'],ClassInteraction([],{},{},['Gun']) ),
                   ObjectClass('Shotgun',['bullet','clip','Shoot()','Reload()'],ClassInteraction(['Weapon'],{},{},['Types','Gun']) ),
                   ObjectClass('Cat',['weapon','voice','Meow()','Kill()'],ClassInteraction(['Animal'],{'weapon':'Weapon'},{},[])),
                   ObjectClass('Dog',[],ClassInteraction(['Animal'],{},{},[])),
                   ObjectClass('Bird',[],ClassInteraction(['Animal'],{},{},[])),
                   ObjectClass('Dogocat',[],ClassInteraction(['Cat','Dog'],{},{},[])),
                   ObjectClass('Pigeon',['pet'],ClassInteraction(['Bird'],{},{'pet':'Dog'},[]))]
        return classes
