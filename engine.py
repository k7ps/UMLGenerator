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
        return self.__example()
        classes = []
        for file in self.__files:
            for cl in file.GetClasses():
                classes.append(cl)
        return classes

    def __example(self):
        classes = [o.ObjectClass('Animal',['point','health','name','Heal()','Upgrade()'],o.ClassInteraction([],{},{},[])),
                   o.ObjectClass('Weapon',['type','damage','Hit()'], o.ClassInteraction([],{},{},['Gun']) ),
                   o.ObjectClass('Shotgun',['bullet','clip','Shoot()','Reload()'], o.ClassInteraction(['Weapon'],{},{},['Gun']) ),
                   o.ObjectClass('Cat',['weapon','voice','Meow()','Kill()'],o.ClassInteraction(['Animal'],{'weapon':'Weapon'},{},[])),
                   o.ObjectClass('Dog',[],o.ClassInteraction(['Animal'],{},{},[])),
                   o.ObjectClass('Bird',[],o.ClassInteraction(['Animal'],{},{},[])),
                   o.ObjectClass('Dogocat',[],o.ClassInteraction(['Cat','Dog'],{},{},[])),
                   o.ObjectClass('Pigeon',['pet'],o.ClassInteraction(['Bird'],{},{'pet':'Dog'},[]))]
        return classes
