class Animal:
    _a = 10
    def __init__(self):
        self.point = 1 
        self.health = 1
        self.name = ""
    def Heal(self):
        self.health=100
    def Upgrade(self):
        self.point += 1

#@UML clusters Gun
class Weapon:
    def __init__(self):
        self.type = None
        self.damage = 10
    def Hit(self, animal):
        animal.health -= damage
        
#@UML clusters Gun, Type
class Shotgun(Weapon):
    def __init__(self):
        self.bullet = 10
        self.clip = 15
    def Shoot(self):
        Hit()
    def Reload(self):
        self.bullet = 10

class Cat(Animal):
    def __init__(self):
        self.weapon: Shotgun = Shotgun()
        self.voice = "meow"
    def Meow(self):
        print(self.voice)
    def Kill(self):
        self.weapon.Shoot()
        
class Dog(Animal):
    pass

class Bird(Animal):
    pass

class Pigeon(Bird):
    def __init__(self, d: Dog):
        self.pet: Dog = d #@UML aggr

class Dogocat(Cat, Dog):
    pass
