from enum import Enum

from settings import *

#@UML clusters ObjectClass
class ClassInteraction:
    def __init__(self, parents, clusters):
        self.__parents = parents
        self.__clusters = clusters

    def GetParents(self):
        return self.__parents

    def GetClusters(self):
        return self.__clusters

    def SetClusters(self, clusters):
        self.__clusters = clusters



#@UML clusters ObjectClass
class Drawable:
    def __init__(self, ignored):
        self.__IsIgnore = ignored

    @property
    def IsIgnore(self):
        return self.__IsIgnore

    @IsIgnore.setter
    def IsIgnore(self, ignored):
        self.__IsIgnore = ignored


#@UML clusters ObjectClass
class AccessMod(Enum):
    PUBLIC = 0
    PROTECTED = 1
    PRIVATE = 2


#@UML clusters ObjectClass
class Field(Drawable):
    def __init__(self, name, ignored):
        super().__init__(ignored)
        self.__name = name

        self.__modifier: AccessMod = AccessMod.PUBLIC
        if name.startswith('__'):
            self.__modifier = AccessMod.PRIVATE
            if Set.ignorePrivate:
                if self.IsVariable() and self.HaveType():
                    self.IsIgnore = Set.ignorePrivateComps
                else:
                    self.IsIgnore = True
        elif name.startswith('_'):
            self.__modifier = AccessMod.PROTECTED
            if Set.ignoreProtected:
                if self.IsVariable() and self.HaveType():
                    self.IsIgnore = Set.ignoreProtectedComps
                else:
                    self.IsIgnore = True

        if Set.removeAccessPrefix:
            if self.__modifier == AccessMod.PRIVATE:
                if not self.__name.endswith('__()'):
                    self.__name = self.__name[2:]
            if self.__modifier == AccessMod.PROTECTED:
                self.__name = self.__name[1:]

    @property
    def modifier(self):
        return self.__modifier

    @property
    def name(self):
        return self.__name

    def IsVariable(self):
        return type(self) is Variable

    def IsMethod(self):
        return type(self) is Method



#@UML clusters ObjectClass
class Variable(Field):
    def __init__(self, name, varType='', isAggr = False, ignored=False):
        self.__type = varType
        self.__isAggr = isAggr
        super().__init__(name, ignored)
    
    @property
    def isAggr(self):
        return self.__isAggr

    def GetType(self):
        return self.__type

    def HaveType(self):
        return self.__type != ''

    
#@UML clusters ObjectClass
class Method(Field):
    def __init__(self, name, ignored=False):
        super().__init__(name+'()', ignored)



#@UML clusters ObjectClass
class ObjectClass(Drawable):
    def __init__(self, name, fields, interactions, ignored=False, filename = ''):
        super().__init__(ignored)
        self.__name = name
        self.__fields: list[Field] = self.__DeleteSame (fields)
        self.__interactions: ClassInteraction = interactions
        self.__fileName = filename
    
    def __DeleteSame(self, array):
        res = []
        for x in array:
            have = False
            for y in res:
                if x.name == y.name:
                    have =True
            if not have:
                res.append(x)
        return res

    def SetFileName(self, name):
        self.__fileName = name
        
        if Set.groupByFiles:
            self.SetClusters([name])

    def Get(self):
        return (self.__name, self.__fields)

    def GetVars(self):
        variables = []
        for field in self.__fields:
            if field.IsVariable():
                variables.append(field)
        return variables

    def GetName(self):
        return self.__name

    def GetParents(self):
        return self.__interactions.GetParents()

    def GetClusters(self):
        return self.__interactions.GetClusters()
    
    def SetClusters(self, clusters):
        self.__interactions.SetClusters (clusters)

    def Print(self):
        print('>', self.__name, "Ignore=", self.IsIgnore)
        print('\tFields:',[i.name for i in self.__fields])
        print('\tParents:', *self.GetParents(), sep='  ')
        print('\tClusters:', *self.GetClusters(), sep='  ')
